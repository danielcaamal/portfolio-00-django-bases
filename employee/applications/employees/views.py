from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, TemplateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Employee
from django.http import HttpResponse, HttpRequest
from django.forms.models import BaseModelForm
import typing


# Create your views here.

class ListAllEmployees(ListView):
    template_name = 'employee/list_all.html'
    paginate_by = 10
    model = Employee
    
class ListEmployeeByArea(ListView):
    template_name = 'employee/list_by_area.html'
    
    def get_queryset(self):
        department_id = self.kwargs['id']
        return Employee.objects.filter(
            department__id=department_id
        )

class ListEmployeesByKWord(ListView):
    template_name = 'employee/list_by_kword.html'
    
    def get_queryset(self):
        k_word = self.request.GET.get('kword', '')
        return Employee.objects.filter(
            first_name__icontains=k_word
        )


class ListEmployeeAbilities(ListView):
    template_name = 'employee/list_abilities.html'
    
    def get_queryset(self):
        employee_id = self.kwargs['id']
        employee = Employee.objects.get(id=employee_id)
        return employee.abilities.all();



class EmployeeDetailView(DetailView):
    model = Employee
    template_name = "employee/detail_employee.html"
    
    def get_context_data(self, **kwargs):
        context = super(EmployeeDetailView, self).get_context_data(**kwargs)
        context["title"] = 'Employee of the month'
        return context
    


class EmployeeCreateView(CreateView):
    model = Employee
    template_name = "employee/create_employee.html"
    fields = (
        'first_name',
        'last_name',
        'email',
        'job',
        'department',
    )
    # fields = ('__all__')
    success_url = reverse_lazy('employee_app:create-employee-success')
    
    def form_valid(self, form):
        empleado = form.save(commit=False)
        empleado.full_name = empleado.first_name + ' ' + empleado.last_name
        empleado.save()
        return super(EmployeeCreateView, self).form_valid(form)


class SuccessView(TemplateView):
    template_name = "employee/create_employee_success.html"
    


class EmployeeUpdateView(UpdateView):
    model = Employee
    template_name = "employee/update_employee.html"
    fields = (
        'first_name',
        'last_name',
        'email',
        'job',
        'department',
        'abilities'
    )
    
    success_url = reverse_lazy('employee_app:list-all-employees')
    
    def post(self, request: HttpRequest, *args: str, **kwargs) -> HttpResponse:
        return super(EmployeeUpdateView, self).post(request, *args, **kwargs)
    
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        return super(EmployeeUpdateView, self).form_valid(form)



class EmployeeDeleteView(DeleteView):
    model = Employee
    template_name = "employee/delete_employee.html"
    success_url = reverse_lazy('employee_app:list-all-employees')
    