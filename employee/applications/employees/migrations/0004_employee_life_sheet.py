# Generated by Django 4.1.7 on 2023-03-23 00:10

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0003_employee_abilities_alter_employee_department'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='life_sheet',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Hoja de vida'),
        ),
    ]
