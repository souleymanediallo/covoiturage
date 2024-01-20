from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('search/', views.search, name='search'),
    path('mentions-legales/', views.mentions, name='mentions-legales'),
    path('conditions-generales/', views.conditons, name='conditions-generales'),
    path('conducteur/', views.conducteur, name='conducteur'),
    path('passager/', views.passager, name='passager'),
    path('contact/', views.contact, name='contact'),
    path('faq/', views.faq, name='faq'),
]