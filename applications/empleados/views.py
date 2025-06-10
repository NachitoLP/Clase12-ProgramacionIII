from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Empleado
from .forms import EmpleadoForm

from django.contrib.auth.mixins import LoginRequiredMixin


class EmpleadoListView(LoginRequiredMixin,ListView):
    model = Empleado
    template_name = 'empleados/empleado_list.html'
    context_object_name = 'empleados'


class EmpleadoDetailView(LoginRequiredMixin,DetailView):
    model = Empleado
    template_name = 'empleados/empleado_detail.html'
    context_object_name = 'empleado'


class EmpleadoCreateView(LoginRequiredMixin,CreateView):
    model = Empleado
    form_class = EmpleadoForm
    template_name = 'empleados/empleado_form.html'
    success_url = reverse_lazy('empleado_list')


class EmpleadoUpdateView(LoginRequiredMixin,UpdateView):
    model = Empleado
    form_class = EmpleadoForm
    template_name = 'empleados/empleado_form.html'
    success_url = reverse_lazy('empleado_list')


class EmpleadoDeleteView(LoginRequiredMixin,DeleteView):
    model = Empleado
    template_name = 'empleados/empleado_confirm_delete.html'
    success_url = reverse_lazy('empleado_list')