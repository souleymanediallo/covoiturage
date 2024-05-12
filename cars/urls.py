from django.urls import path
from . import views


urlpatterns = [
    path('', views.CarListView.as_view(), name='car_list'),
    path('create/', views.CarCreateView.as_view(), name='car_create'),
    path('update/<int:pk>/', views.CarUpdateView.as_view(), name='car_update'),
    path('delete/<int:pk>/', views.CarDeleteView.as_view(), name='car_delete'),
    path('detail/<int:pk>/', views.CarDetailView.as_view(), name='car_detail'),
]