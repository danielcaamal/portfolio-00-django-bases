# Generated by Django 4.1.7 on 2023-03-22 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('department', '0002_alter_department_name_alter_department_short_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='department',
            options={'ordering': ['name'], 'verbose_name': 'Mi área', 'verbose_name_plural': 'Áreas de la empresa'},
        ),
        migrations.AlterField(
            model_name='department',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Nombre'),
        ),
        migrations.AlterUniqueTogether(
            name='department',
            unique_together={('name', 'short_name')},
        ),
    ]