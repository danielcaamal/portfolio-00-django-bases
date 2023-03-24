"""employee URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import ListAllEmployees, ListEmployeeByArea, \
    ListEmployeesByKWord, ListEmployeeAbilities, EmployeeDetailView, \
    EmployeeCreateView, SuccessView, EmployeeUpdateView, EmployeeDeleteView

app_name = "employee_app"

urlpatterns = [
    path('list-all-employees/', ListAllEmployees.as_view(), name="list-all-employees"),
    path('list-all-employees-by-area/<id>/', ListEmployeeByArea.as_view(), name="list-all-employees-by-area"),
    path('search/<kword>/', ListEmployeesByKWord.as_view(), name="list-all-employees-by-k-word"),
    path('abilities/<id>', ListEmployeeAbilities.as_view(), name="list-all-abilities-by-employee"),
    path('detail/<pk>', EmployeeDetailView.as_view(), name="detail-employee"),
    path('create/', EmployeeCreateView.as_view(), name="create-employee"),
    path('create-success/', SuccessView.as_view(), name="create-employee-success"),
    path('update/<pk>', EmployeeUpdateView.as_view(), name="update-employee"),
    path('delete/<pk>', EmployeeDeleteView.as_view(), name="delete-employee"),
]
