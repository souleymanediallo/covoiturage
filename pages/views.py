from django.shortcuts import render
from django.views.generic import TemplateView
from trips.models import Trip
from datetime import datetime
from trips.city import CITY_SENEGAL


today_current = datetime.today().strftime('%Y-%m-%d')
time_trip = datetime.now().strftime('%H:%M')


class HomePageView(TemplateView):
    template_name = 'pages/index.html'

    ordering = ['start_date', 'start_time']

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['trips'] = Trip.objects.filter(start_date__gte=today_current)
        context['city_senegal'] = CITY_SENEGAL
        return context
