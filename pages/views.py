from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.http import Http404
from django.views.generic import TemplateView
from trips.models import Trip
from datetime import datetime
from django.utils import timezone
from trips.city import CITY_SENEGAL
from covoiturages.models import Covoiturage
from homework.models import Homework


today_current = datetime.today().strftime('%Y-%m-%d')
time_trip = datetime.now().strftime('%H:%M')


class HomePageView(TemplateView):
    template_name = 'pages/index.html'

    ordering = ['start_date', 'start_time']

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        now = timezone.now()
        context['homeworks'] = Homework.objects.all().order_by('-created_at')[:6]
        context['trips'] = Trip.objects.filter(
            start_date__gt=now.date()
        ) | Trip.objects.filter(
            start_date=now.date(),
            start_time__gte=now.time()
        ).order_by('start_date', 'start_time')[:4]

        context['city_senegal'] = CITY_SENEGAL
        return context


# def search(request):
#     return render(request, 'pages/search.html')


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


def mentions_cgu(request):
    return render(request, 'pages/mentions-legales.html')


def conditons(request):
    return render(request, 'pages/conditions-generales.html')


def conducteur(request):
    return render(request, 'pages/conducteur.html')


def passager(request):
    return render(request, 'pages/passager.html')


def faq(request):
    return render(request, 'pages/aide.html')


def page_404(request):
    raise Http404("Page non trouvée")


@login_required
def published_trips(request):
    return render(request, 'pages/publier-trajet.html')


def robots_txt(request):
    lines = [
        "User-agent: *",
        "Disallow: /admin/",
        "Disallow: /accounts/",

        "Allow: /",
        "Sitemap: https://www.covoiturage.sn/sitemap.xml",
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")