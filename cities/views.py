from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import City
# Create your views here.


class DetailCityView(DetailView):
    model = City
    template_name = 'cities/city_detail.html'
    context_object_name = 'city'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['city'] = City.objects.get(slug=self.kwargs['slug'])
        return context

    def get_object(self, queryset=None):
        return City.objects.get(slug=self.kwargs['slug'])

