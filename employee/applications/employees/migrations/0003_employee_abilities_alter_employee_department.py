# Generated by Django 4.1.7 on 2023-03-22 23:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('department', '0003_alter_department_options_alter_department_name_and_more'),
        ('employees', '0002_abilities_alter_employee_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='abilities',
            field=models.ManyToManyField(to='employees.abilities', verbose_name='Habilidades'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='department',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='department.department', verbose_name='Areas'),
        ),
    ]
