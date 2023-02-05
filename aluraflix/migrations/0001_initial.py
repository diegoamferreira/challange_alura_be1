# Generated by Django 4.1.6 on 2023-02-05 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=30, verbose_name='Título')),
                ('descricao', models.TextField(verbose_name='Descrição')),
                ('url', models.URLField(verbose_name='URL')),
            ],
        ),
    ]
