from django.contrib import admin
from .models import Category, Post, PostImage


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "is_indexable")
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ("name", "description")
    list_filter = ("is_indexable",)


class PostImageInline(admin.TabularInline):
    model = PostImage
    extra = 0


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "status", "publish_at", "category", "is_featured", "is_indexable", "reading_time_min")
    list_filter = ("status", "category", "is_featured", "is_indexable")
    search_fields = ("title", "content", "meta_title", "meta_description")
    prepopulated_fields = {"slug": ("title",)}
    date_hierarchy = "publish_at"
    inlines = [PostImageInline]
    readonly_fields = ("reading_time_min",)
