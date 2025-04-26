from django.urls import path
from . import views

urlpatterns = [
    path('', views.BusLineListView.as_view(), name='bus_lines'),
    path('ligne/<str:number>/<slug:departure_slug>/<slug:arrival_slug>/', views.BusLineDetailView.as_view(), name='bus_line_detail'),  # Détail d'une ligne
    path('arret/<int:pk>/', views.StopDetailView.as_view(), name='stop_detail'),
]