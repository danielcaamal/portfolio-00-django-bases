# Generated by Django 4.1.7 on 2023-03-23 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0004_employee_life_sheet'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='fullname',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Nombre completo'),
        ),
    ]
