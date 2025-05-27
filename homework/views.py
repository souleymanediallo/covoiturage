from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages

from .forms import HomeworkForm
from .models import Homework, DAYS_OF_WEEK


class HomeworkCreateView(LoginRequiredMixin, CreateView):
    model = Homework
    form_class = HomeworkForm
    template_name = 'homework/homework_form.html'
    success_url = reverse_lazy('homework_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        form = ctx['form']
        # Construire la liste des lignes du planning
        schedule_rows = []
        for code, label in DAYS_OF_WEEK:
            # Nom des champs dans le form
            active_name = f"{code}_active"
            start_name = f"{code}_start"
            end_name = f"{code}_end"

            # Récupère les BoundField du form
            schedule_rows.append({
                'label': label,
                'active': form[active_name],
                'start': form[start_name],
                'end': form[end_name],
            })

        ctx['schedule_rows'] = schedule_rows
        return ctx


class HomeworkListView(ListView):
    model = Homework
    template_name = 'homework/homework_list.html'
    context_object_name = 'homeworks'
    ordering = ['-created_at']
    paginate_by = 5


class HomeworkDetailView(DetailView):
    model = Homework
    template_name = 'homework/homework_detail.html'
    context_object_name = 'homework'

    def get_object(self):
        # Récupérer l'ID abrégé à partir de l'URL
        id_abbr = self.kwargs.get("id_abbr")

        # Rechercher l'objet Homework uniquement basé sur l'ID abrégé
        trip = get_object_or_404(Homework, id__startswith=id_abbr)
        return trip

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        hw = self.object

        # Construire une liste de jours activés
        active_rows = []
        for code, label in DAYS_OF_WEEK:
            if getattr(hw, f"{code}_active"):
                active_rows.append({
                    'label': label,
                    'start': getattr(hw, f"{code}_start"),
                    'end':   getattr(hw, f"{code}_end"),
                })

        ctx['active_rows'] = active_rows
        return ctx


class HomeworkUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Homework
    form_class = HomeworkForm
    template_name = 'homework/homework_form.html'
    success_url = reverse_lazy('homework_list')

    def get_object(self):
        # Récupérer l'ID abrégé à partir de l'URL
        id_abbr = self.kwargs.get("id_abbr")
        # Rechercher l'objet Homework uniquement basé sur l'ID abrégé
        trip = get_object_or_404(Homework, id__startswith=id_abbr)
        return trip

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        form = ctx['form']
        # Construire la liste des lignes du planning
        schedule_rows = []
        for code, label in DAYS_OF_WEEK:
            # Nom des champs dans le form
            active_name = f"{code}_active"
            start_name = f"{code}_start"
            end_name = f"{code}_end"

            # Récupère les BoundField du form
            schedule_rows.append({
                'label': label,
                'active': form[active_name],
                'start': form[start_name],
                'end': form[end_name],
            })

        ctx['schedule_rows'] = schedule_rows
        return ctx

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        homework = self.get_object()
        return self.request.user == homework.author or self.request.user.is_superuser




class HomeworkDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Homework
    template_name = 'homework/homework_confirm_delete.html'
    success_url = reverse_lazy('homework_list')

    def get_object(self):
        # Récupérer l'ID abrégé à partir de l'URL
        id_abbr = self.kwargs.get("id_abbr")
        # Rechercher l'objet Homework uniquement basé sur l'ID abrégé
        trip = get_object_or_404(Homework, id__startswith=id_abbr)
        return trip

    def test_func(self):
        homework = self.get_object()
        return self.request.user == homework.author or self.request.user.is_superuser

    def handle_no_permission(self):
        messages.error(self.request, "Vous n'avez pas la permission de supprimer cette tâche.")
        return super().handle_no_permission()



