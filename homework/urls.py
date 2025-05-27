from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomeworkListView.as_view(), name='homework_list'),
    path('<slug:start_city_slug>-<slug:end_city_slug>/<str:id_abbr>', views.HomeworkDetailView.as_view(), name='homework-detail'),
    path('create/', views.HomeworkCreateView.as_view(), name='homework-create'),
    path('update/<slug:start_city_slug>-<slug:end_city_slug>/<str:id_abbr>', views.HomeworkUpdateView.as_view(), name='homework-update'),
    path('delete/<slug:start_city_slug>-<slug:end_city_slug>/<str:id_abbr>', views.HomeworkDeleteView.as_view(), name='homework-delete'),
]
