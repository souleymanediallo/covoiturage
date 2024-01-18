from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('search/', views.search, name='search'),
    path('mentions/', views.mentions, name='mentions'),
    path('conditions/', views.conditons, name='conditions'),
    path('conducteur/', views.conducteur, name='conducteur'),
    path('passager/', views.passager, name='passager'),
    path('contact/', views.contact, name='contact'),
]