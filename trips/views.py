from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import View
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from .forms import TripForm
from .models import Trip
# Create your views here.
from datetime import datetime
today_current = datetime.today().strftime('%Y-%m-%d')
time_expired = datetime.now().strftime('%H:%M')


class TripListView(ListView):
    model = Trip
    template_name = 'trips/trip_list.html'
    context_object_name = 'trips'
    ordering = ['-start_date', '-start_time']
    paginate_by = 5

    def get_queryset(self):
        return Trip.objects.filter(start_date__gte=today_current, start_time__gte=time_expired)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['today_current'] = today_current
        context['time_expired'] = time_expired
        return context


class TripCreateView(LoginRequiredMixin, CreateView):
    model = Trip
    form_class = TripForm
    context_object_name = "form"
    success_url = reverse_lazy('home')
    template_name = 'trips/trip_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)