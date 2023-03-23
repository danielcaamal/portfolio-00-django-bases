from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('list', views.ModelTestListView.as_view(), name='test_list'),
]
