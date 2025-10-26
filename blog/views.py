# blog/views.py
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Post, Category


class PostListView(ListView):
    queryset = Post.objects.published().select_related("category")
    template_name = "blog/post_list.html"
    context_object_name = "posts"


class CategoryListView(ListView):
    queryset = Category.objects.all()
    template_name = "blog/category_list.html"
    context_object_name = "categories"


class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    slug_field = "slug"
    slug_url_kwarg = "slug"

    def get_queryset(self):
        return Post.objects.published().select_related("author", "category")

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        post = self.object
        ctx["prev_post"] = (Post.objects.published()
                            .filter(publish_at__lt=post.publish_at)
                            .order_by("-publish_at")
                            .first())
        ctx["next_post"] = (Post.objects.published()
                            .filter(publish_at__gt=post.publish_at)
                            .order_by("publish_at")
                            .first())
        return ctx


class CategoryDetailView(ListView):
    template_name = "blog/category_detail.html"
    context_object_name = "posts"
    paginate_by = 10

    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)
        # défini une fois pour toute
        self.category = get_object_or_404(Category, slug=kwargs["slug"])

    def get_queryset(self):
        return (Post.objects.published()
                .filter(category=self.category)
                .select_related("category", "author"))

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["category"] = self.category
        return ctx
