# covoiturage/templatetags/pluralize_places.py
from django import template

register = template.Library()

@register.filter(name='places')
def places(value):
    try:
        n = int(value)
    except (ValueError, TypeError):
        return ''
    return '' if n in (0, 1) else 's'