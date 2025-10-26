from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.utils import timezone
import re
from django_ckeditor_5.fields import CKEditor5Field


# ---------- Mixins ----------
class TimeStamped(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True)

    class Meta:
        abstract = True


class SeoFields(models.Model):
    # Contrôle d’indexation
    is_indexable = models.BooleanField(default=True, help_text="Décoche pour noindex.")
    follow_links = models.BooleanField(default=True, help_text="Décoche pour nofollow.")

    # Balises meta
    meta_title = models.CharField(max_length=70, blank=True, help_text="≤ 60–70 caractères.")
    meta_description = models.TextField(blank=True, help_text="≤ 155–160 caractères.")

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if self.meta_title and len(self.meta_title) > 70:
            self.meta_title = self.meta_title[:70]
        if self.meta_description and len(self.meta_description) > 160:
            self.meta_description = self.meta_description[:160]
        super().save(*args, **kwargs)

    # pratique pour le template <meta name="robots">
    def robots_meta(self) -> str:
        return f"{'index' if self.is_indexable else 'noindex'}, {'follow' if self.follow_links else 'nofollow'}"

    @staticmethod
    def _text_only(value: str) -> str:
        # enlève balises HTML et compresse les espaces
        text = re.sub(r"<[^>]+>", " ", value or "")
        return re.sub(r"\s+", " ", text).strip()

# ---------- Post ----------
def upload_cover(instance, filename):
    return f"blog/covers/{instance.slug}/{filename}"

def upload_inline_image(instance, filename):
    # instance = PostImage, donc on utilise la FK déjà posée
    return f"blog/images/{instance.post_id}/{filename}"


class Category(TimeStamped, SeoFields):
    name = models.CharField(max_length=120, unique=True)
    slug = models.SlugField(max_length=140, unique=True)
    cover = models.ImageField(upload_to=upload_cover, blank=True, null=True)
    cover_alt = models.CharField(max_length=125, blank=True)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name = "Catégorie"
        verbose_name_plural = "Catégories"
        ordering = ["name"]
        indexes = [models.Index(fields=["slug"])]

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        if not self.meta_title:
            self.meta_title = self.name[:70]
        if not self.meta_description and self.description:
            self.meta_description = SeoFields._text_only(self.description)[:160]
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("blog:category_detail", args=[self.slug])

    def post_count(self) -> int:
        return self.posts.filter(is_deleted=False).count()


class PostQuerySet(models.QuerySet):
    def published(self):
        now = timezone.now()
        return self.filter(status=Post.Status.PUBLISHED, publish_at__lte=now, is_deleted=False)

    def scheduled(self):
        return self.filter(status=Post.Status.SCHEDULED, is_deleted=False)


class Post(TimeStamped, SeoFields):
    class Status(models.TextChoices):
        DRAFT = "draft", "Brouillon"
        SCHEDULED = "scheduled", "Programmé"
        PUBLISHED = "published", "Publié"

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name="blog_posts"
    )
    title = models.CharField(max_length=160, db_index=True)
    slug = models.SlugField(max_length=180, unique=True)
    content = CKEditor5Field("Contenu", config_name='blog_ckeditor', blank=True, null=True, help_text="Contenu de l’article.")
    cover = models.ImageField(upload_to=upload_cover, blank=True, null=True)
    cover_alt = models.CharField(max_length=125, blank=True)

    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name="posts")

    status = models.CharField(max_length=10, choices=Status.choices, default=Status.DRAFT, db_index=True)
    publish_at = models.DateTimeField(default=timezone.now, db_index=True)
    is_featured = models.BooleanField(default=False, help_text="Mise en avant (homepage, blocs SEO).")
    is_deleted = models.BooleanField(default=False)

    # SEO/UX
    reading_time_min = models.PositiveSmallIntegerField(default=1, help_text="Temps de lecture estimé.")

    objects = PostQuerySet.as_manager()

    class Meta:
        ordering = ["-publish_at"]
        indexes = [
            models.Index(fields=["status", "publish_at"]),
            models.Index(fields=["slug"]),
        ]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:post_detail", args=[self.slug])

    # Helpers
    def _estimate_reading_time(self):
        # ~200 mots/min, sur texte brut
        words = len(re.findall(r"\w+", SeoFields._text_only(self.content)))
        return max(1, round(words / 200))

    @property
    def content_preview(self) -> str:
        """A utiliser dans les listes pour simuler l'excerpt (ex: 35–55 mots)."""
        text = SeoFields._text_only(self.content)
        words = text.split()
        return " ".join(words[:50]) + ("…" if len(words) > 50 else "")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)[:175]
        # Métas par défaut
        if not self.meta_title:
            self.meta_title = self.title[:70]
        if not self.meta_description:
            self.meta_description = SeoFields._text_only(self.content)[:160]
        # Estimation temps de lecture
        self.reading_time_min = self._estimate_reading_time()
        super().save(*args, **kwargs)


class PostImage(TimeStamped):
    """Images dans le corps d’un article, avec balise alt pour SEO/Accessibilité."""
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to=upload_inline_image)
    alt_text = models.CharField(max_length=125, help_text="Texte alternatif (obligatoire).")

    def __str__(self):
        return f"Image for {self.post_id}"
