# blog/urls.py
from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("", views.CategoryListView.as_view(), name="category_list"),
    path("<slug:slug>/", views.PostDetailView.as_view(), name="post_detail"),
    path("categorie/<slug:slug>/", views.CategoryDetailView.as_view(), name="category_detail"),
]
