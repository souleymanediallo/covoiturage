from django import template
from blog.models import Category, Post
register = template.Library()


@register.simple_tag(name="categories")
def all_categories():
    return Category.objects.all()


@register.simple_tag
def recent_posts(exclude_post_id=None, count=3):
    return Post.objects.exclude(id=exclude_post_id).order_by("-created_at")[:count]