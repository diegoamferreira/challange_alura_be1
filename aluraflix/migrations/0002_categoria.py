# Generated by Django 4.1.6 on 2023-02-05 12:15

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aluraflix', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=30, verbose_name='Titulo')),
                ('cor', models.CharField(max_length=7, validators=[django.core.validators.RegexValidator(message='Color must be Hexadecimal code', regex='^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$')], verbose_name='Cor')),
            ],
        ),
    ]