from django.db import models

# Create your models here.

class Test(models.Model):
    title = models.CharField(max_length=30)
    subtitle = models.CharField(max_length=50)
