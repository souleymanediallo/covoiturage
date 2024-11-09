from django import template
from django.db.models import Value
from django.db.models.functions import Lower
from trips.models import Trip
from trips.city import CITY_SENEGAL
import unicodedata

register = template.Library()


def normalize_string(value):
    return ''.join(
        c for c in unicodedata.normalize('NFD', value)
        if unicodedata.category(c) != 'Mn'
    ).lower()


@register.inclusion_tag('partials/search.html', takes_context=True)
def show_search_results(context):
    request = context['request']
    trips = Trip.objects.annotate(
        normalized_start_city=Lower('start_city'),
        normalized_end_city=Lower('end_city')
    )

    if 'start_city' in request.GET:
        start_city = request.GET['start_city']
        if start_city:
            normalized_start_city = normalize_string(start_city)
            trips = trips.filter(
                normalized_start_city__icontains=normalized_start_city
            )

    if 'end_city' in request.GET:
        end_city = request.GET['end_city']
        if end_city:
            normalized_end_city = normalize_string(end_city)
            trips = trips.filter(
                normalized_end_city__icontains=normalized_end_city
            )

    return {
        'city_senegal': CITY_SENEGAL,
        'trips': trips,
        'values': request.GET,
    }
