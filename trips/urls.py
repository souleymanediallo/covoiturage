from django.urls import path
#from .views import RequestBookingView, AcceptBookingView, CancelBookingView, RejectBookingView
from . import views

urlpatterns = [
    path('create', views.TripCreateView.as_view(), name='trip-create'),
    path('', views.TripListView.as_view(), name='trip-list'),
    path('<slug:short_uuid>', views.TripDetailView.as_view(), name='trip-detail'),
    path('my-trip-list', views.my_trip, name='my-trips'),
    path('<str:pk>/update', views.TripUpdateView.as_view(), name='trip-update'),
    path('<str:pk>/delete', views.TripDeleteView.as_view(), name='trip-delete'),
    path('<trip_id>/reservation', views.trip_reservation, name='trip-reservation'),
    # Booking
    #path('<trip_id>/booking/request/', RequestBookingView.as_view(), name='request_booking'),
    #path('booking/<uuid:pk>/accept/', AcceptBookingView.as_view(), name='accept_booking'),
    #path('booking/<uuid:pk>/cancel/', CancelBookingView.as_view(), name='cancel_booking'),
    #path('booking/<uuid:pk>/reject/', RejectBookingView.as_view(), name='reject_booking'),
]