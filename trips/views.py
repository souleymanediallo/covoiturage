from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import View
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from .forms import TripForm
from .models import Trip, Reservation
# Create your views here.
from datetime import datetime
today_current = datetime.today().strftime('%Y-%m-%d')
time_expired = datetime.now().strftime('%H:%M')


class TripListView(ListView):
    model = Trip
    template_name = 'trips/trip_list.html'
    context_object_name = 'trips'
    ordering = ['start_date', 'start_time']
    paginate_by = 5


class TripCreateView(LoginRequiredMixin, CreateView):
    model = Trip
    form_class = TripForm
    context_object_name = "form"
    success_url = reverse_lazy('home')
    template_name = 'trips/trip_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class TripDetailView(DetailView):
    model = Trip
    template_name = 'trips/trip_detail.html'
    context_object_name = 'trip'


class TripUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Trip
    form_class = TripForm
    context_object_name = "form"
    success_url = reverse_lazy('dashboard')
    template_name = 'trips/trip_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        trip = self.get_object()
        if self.request.user == trip.author:
            return True
        return False


class TripDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Trip
    success_url = reverse_lazy('dashboard')
    template_name = 'trips/trip_confirm_delete.html'

    def test_func(self):
        trip = self.get_object()
        if self.request.user == trip.author:
            return True
        return False


@login_required
def my_trip(request):
    trips = Trip.objects.all()
    context = {"trips": trips}
    return render(request, "trips/my-trip-list.html", context)


@login_required
def trip_reservation(request, trip_id):
    trip = get_object_or_404(Trip, pk=trip_id)

    if request.method == 'POST':
        seats_reserved_go = int(request.POST.get('seats_reserved_go', 0))
        seats_reserved_back = int(request.POST.get('seats_reserved_back', 0))

        # Vérifier les places disponibles pour l'aller
        if seats_reserved_go > trip.available_seats('Aller Simple'):
            messages.error(request, "Le nombre de places demandées pour l'aller est supérieur au nombre de places disponibles.")
            return redirect('trip-detail', trip_id)

        # Vérifier les places disponibles pour le retour
        if seats_reserved_back > trip.available_seats('Aller Retour'):
            messages.error(request, "Le nombre de places demandées pour le retour est supérieur au nombre de places disponibles.")
            return redirect('trip-detail', trip_id)

        # Créer la réservation pour l'aller
        if seats_reserved_go > 0:
            Reservation.objects.create(
                trip=trip,
                passenger=request.user,
                seats_reserved_go=seats_reserved_go
            )

        # Créer la réservation pour le retour
        if seats_reserved_back > 0:
            Reservation.objects.create(
                trip=trip,
                passenger=request.user,
                seats_reserved_back=seats_reserved_back
            )

        messages.success(request, "Votre réservation a été enregistrée avec succès.")
        return redirect('trip-detail', trip_id)

    else:
        context = {'trip': trip}
        return render(request, 'trips/trip_reservation.html', context)
