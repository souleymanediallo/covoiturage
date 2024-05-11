from django.db import models
import uuid

from django.utils.text import slugify


# Create your models here.
class Destination(models.Model):
    name = models.CharField(max_length=200)
    desc = models.TextField(blank=True, null=True)
    slug = models.SlugField(max_length=200, unique=True)

    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Destination, self).save(*args, **kwargs)

    def __str__(self):
        return self.name