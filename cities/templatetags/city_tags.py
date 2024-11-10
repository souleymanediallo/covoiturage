from django import template
from cities.models import City

register = template.Library()


@register.inclusion_tag('cities/city_list.html')
def show_all_cities():
    cities = City.objects.all().order_by('name')
    return {'cities': cities}