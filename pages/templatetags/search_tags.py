from django import template
from trips.models import Trip
from covoiturages.models import Covoiturage
from trips.city import CITY_SENEGAL
register = template.Library()


@register.inclusion_tag('partials/search.html', takes_context=True)
def show_search_results(context):
    request = context['request']
    queryset_list_regular = Trip.objects.all()
    queryset_list_occasional = Covoiturage.objects.all()

    if 'start_city' in request.GET:
        start_city = request.GET['start_city']
        if start_city:
            queryset_list_regular = queryset_list_regular.filter(start_city__iexact=start_city)
            queryset_list_occasional = queryset_list_occasional.filter(start_city__iexact=start_city)

    if 'end_city' in request.GET:
        end_city = request.GET['end_city']
        if end_city:
            queryset_list_regular = queryset_list_regular.filter(end_city__iexact=end_city)
            queryset_list_occasional = queryset_list_occasional.filter(end_city__iexact=end_city)

    return {
        'city_senegal': CITY_SENEGAL,
        'regular': queryset_list_regular,
        'occasional': queryset_list_occasional,
        'values': request.GET,
    }
