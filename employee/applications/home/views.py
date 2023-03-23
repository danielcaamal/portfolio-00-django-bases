from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Test

# Create your views here.

class IndexView(TemplateView):
    template_name = 'home/home.html'
    
    
class TestListView(ListView):
    template_name = 'home/test_list.html'
    queryset = ['one', 'two', 'three','four', 'five']
    context_object_name = 'test_list'
    
    
class ModelTestListView(ListView):
    template_name = 'home/test_list.html'
    model = Test
    context_object_name = 'test_list'