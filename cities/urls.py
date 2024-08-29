from django.urls import path
from . import views

urlpatterns = [
    path('<slug:slug>/', views.DetailCityView.as_view(), name='city-detail'),
]