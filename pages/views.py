from django.shortcuts import render
from django.views.generic import TemplateView
from trips.models import Trip
from datetime import datetime


today_current = datetime.today().strftime('%Y-%m-%d')
time_trip = datetime.now().strftime('%H:%M')


class HomePageView(TemplateView):
    template_name = 'pages/index.html'

    ordering = ['-start_date', '-start_time']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['trips'] = Trip.objects.all()
        return context
