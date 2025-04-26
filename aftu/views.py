from django.shortcuts import render, get_object_or_404
from django.views.generic import View, ListView, DetailView
from django.utils.text import slugify
from django.http import Http404
from django.core.paginator import Paginator

from .models import BusLine, Stop


# Create your views here.
class BusLineListView(ListView):
    model = BusLine
    template_name = 'aftu/bus_lines.html'
    context_object_name = 'lines'
    paginate_by = 20


class BusLineDetailView(View):
    template_name = 'aftu/bus_line_detail.html'

    def get_context_data(self, number, departure_slug, arrival_slug):
        lines = BusLine.objects.filter(number=number)

        for line in lines:
            dep = slugify(line.departure)
            arr = slugify(line.arrival)
            if dep == departure_slug and arr == arrival_slug:
                stops = line.busstop_set.select_related('stop')
                return {
                    'line': line,
                    'stops': stops,
                }

        raise Http404("Ligne non trouvée")

    def get(self, request, number, departure_slug, arrival_slug):
        context = self.get_context_data(number, departure_slug, arrival_slug)
        return render(request, self.template_name, context)


class StopDetailView(DetailView):
    model = Stop
    template_name = 'aftu/stop_detail.html'
    context_object_name = 'stop'  # pour utiliser {{ stop }} dans ton template

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Ajoute les lignes associées à cet arrêt
        context['lines'] = self.object.busline_set.all()
        return context