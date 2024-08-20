from django.urls import path
from . import views

urlpatterns = [
    path('', views.CovoiturageListView.as_view(), name='covoiturage_list'),
    path('<uuid:pk>/', views.CovoiturageDetailView.as_view(), name='covoiturage_detail'),
    path('create/', views.CovoiturageCreateView.as_view(), name='covoiturage_create'),
    path('<uuid:pk>/update/', views.CovoiturageUpdateView.as_view(), name='covoiturage_update'),
    path('<uuid:pk>/delete/', views.CovoiturageDeleteView.as_view(), name='covoiturage_delete'),
]