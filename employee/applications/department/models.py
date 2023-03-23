from django.db import models

# Create your models here.

class Department(models.Model):
    name = models.CharField('Nombre', max_length=50)
    short_name = models.CharField('Nombre corto', max_length=20, unique=True)
    is_active = models.BooleanField('¿Está activo?', default=True)
    
    class Meta:
        verbose_name = 'Mi área'
        verbose_name_plural = 'Áreas de la empresa'
        ordering = ['name']
        unique_together = ('name', 'short_name')
    
    def __str__(self) -> str:
        return f'{self.name} ({self.short_name})'
