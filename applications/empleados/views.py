from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Empleado

class EmpleadoListView(ListView):
    model = Empleado
    template_name = 'empleados/empleado_list.html'
    context_object_name = 'empleados'


class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = 'empleados/empleado_detail.html'
    context_object_name = 'empleado'


class EmpleadoCreateView(CreateView):
    model = Empleado
    template_name = 'empleados/empleado_form.html'
    fields = ['nombreEmp', 'apellidoEmp', 'rolEmp', 'departamentoEmp', 'fechaNac', 'observaciones']
    success_url = reverse_lazy('empleado_list')


class EmpleadoUpdateView(UpdateView):
    model = Empleado
    template_name = 'empleados/empleado_form.html'
    fields = ['nombreEmp', 'apellidoEmp', 'rolEmp', 'departamentoEmp', 'fechaNac', 'observaciones']
    success_url = reverse_lazy('empleado_list')


class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = 'empleados/empleado_confirm_delete.html'
    success_url = reverse_lazy('empleado_list')