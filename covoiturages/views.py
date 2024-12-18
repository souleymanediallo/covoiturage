from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Covoiturage
from .forms import CovoiturageForm


# Create your views here.
class CovoiturageListView(ListView):
    model = Covoiturage
    template_name = 'covoiturages/covoiturage_list.html'
    context_object_name = 'covoiturages'
    paginate_by = 5


class CovoiturageDetailView(DetailView):
    model = Covoiturage
    template_name = 'covoiturages/covoiturage_detail.html'
    context_object_name = 'covoiturage'

    def get_object(self):
        # Récupérer l'ID abrégé à partir de l'URL
        id_abbr = self.kwargs.get("id_abbr")

        # Rechercher l'objet Trip uniquement basé sur l'ID abrégé
        covoiturage = get_object_or_404(Covoiturage, id__startswith=id_abbr)
        return covoiturage


class CovoiturageCreateView(LoginRequiredMixin, CreateView):
    model = Covoiturage
    template_name = 'covoiturages/covoiturage_form.html'
    form_class = CovoiturageForm
    print(form_class)
    success_url = reverse_lazy('covoiturage_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class CovoiturageUpdateView(LoginRequiredMixin, UpdateView):
    model = Covoiturage
    template_name = 'covoiturages/covoiturage_form.html'
    form_class = CovoiturageForm
    success_url = reverse_lazy('covoiturage_list')


class CovoiturageDeleteView(LoginRequiredMixin, DeleteView):
    model = Covoiturage
    template_name = 'covoiturages/covoiturage_confirm_delete.html'
    success_url = reverse_lazy('covoiturage_list')

    def get_queryset(self):
        return self.model.objects.filter(author=self.request.user)


@login_required
def my_covoiturage(request):
    covoiturages = Covoiturage.objects.filter(author=request.user)
    context = {"covoiturages": covoiturages}
    return render(request, "covoiturages/my-covoiturage.html", context)