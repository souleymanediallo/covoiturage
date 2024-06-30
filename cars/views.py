from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import CarForm
from .models import Car

# Create your views here.


class CarListView(ListView):
    model = Car
    template_name = 'cars/car_list.html'
    context_object_name = 'cars'
    ordering = ['brand', 'model']
    paginate_by = 5


class CarCreateView(LoginRequiredMixin, CreateView):
    model = Car
    form_class = CarForm
    context_object_name = "form"
    success_url = reverse_lazy('car_list')
    template_name = 'cars/car_form.html'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class CarDetailView(DetailView):
    model = Car
    template_name = 'cars/car_detail.html'
    context_object_name = 'car'


class CarUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Car
    form_class = CarForm
    context_object_name = "form"
    success_url = reverse_lazy('car_list')
    template_name = 'cars/car_form.html'

    def test_func(self):
        car = self.get_object()
        return self.request.user == car.owner


class CarDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Car
    success_url = reverse_lazy('car_list')
    template_name = 'cars/car_confirm_delete.html'

    def test_func(self):
        car = self.get_object()
        return self.request.user == car.owner