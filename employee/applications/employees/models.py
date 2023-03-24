from django.db import models
from applications.department.models import Department
from ckeditor.fields import RichTextField

# Create your models here.

JOB_CHOICES = (
    ('0', 'Contador'),
    ('1', 'Administrador'),
    ('2', 'Economista'),
    ('3', 'Otro')
)

class Abilities(models.Model):
    """Model definition for Abilities"""
    ability = models.CharField('Habilidad', max_length=50)
    
    class Meta:
        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habilidades'
        
    def __str__(self) -> str:
        return self.ability


class Employee(models.Model):
    """Model definition for Employee"""
    first_name = models.CharField('Nombre', max_length=50)
    last_name = models.CharField('Apellido', max_length=50)
    fullname = models.CharField('Nombre completo', blank=True, null=True, max_length=100)
    email = models.EmailField('Correo electrónico', max_length=254, unique=True)
    job = models.CharField('Cargo', max_length=3, choices=JOB_CHOICES)
    department = models.ForeignKey(Department, verbose_name="Areas", on_delete=models.SET_NULL, null=True)
    # image = models.ImageField('Imagen', upload_to='employee', null=True, blank=True)
    abilities = models.ManyToManyField(Abilities, verbose_name='Habilidades')
    life_sheet = RichTextField('Hoja de vida', null=True, blank=True)
    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
        ordering = ['first_name', 'last_name']
    
    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name} ({self.email}) '