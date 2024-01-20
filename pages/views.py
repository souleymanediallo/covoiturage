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


def search(request):
    queryset_list = Trip.objects.order_by('-start_date', 'start_time')
    if 'start_city' in request.GET:
        start_city = request.GET['start_city']
        if start_city:
            queryset_list = queryset_list.filter(start_city__iexact=start_city)
    if 'end_city' in request.GET:
        end_city = request.GET['end_city']
        if end_city:
            queryset_list = queryset_list.filter(end_city__iexact=end_city)

    context = {
        'city_senegal': CITY_SENEGAL,
        'trips': queryset_list,
        'values': request.GET
    }
    
    return render(request, 'pages/search.html', context)


def mentions(request):
    return render(request, 'pages/mentions-legales.html')


def conditons(request):
    return render(request, 'pages/conditions-generales.html')


def conducteur(request):
    return render(request, 'pages/conducteur.html')


def passager(request):
    return render(request, 'pages/passager.html')


def contact(request):
    return render(request, 'pages/contact.html')


def faq(request):
    return render(request, 'pages/aide.html')