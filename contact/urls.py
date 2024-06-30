from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact, name="contact"),
    path('sent-email/', views.sent_email, name="sent-email"),
]