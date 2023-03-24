from django.contrib import admin
from .models import Employee, Abilities

# Register your models here.
admin.site.register(Abilities)

class EmployeeAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'first_name',
        'last_name',
        'email',
        'job',
        'department',
        'full_name',
    )
    
    def full_name(self, obj):
        return f'{obj.first_name} {obj.last_name}'
    
    search_fields = (
        'first_name',
        'last_name',
        'email',
    )
    
    list_filter = (
        'department',
        'job',
        'abilities',
    )
    
    filter_horizontal = (
        'abilities',
    )
    
    

admin.site.register(Employee, EmployeeAdmin)