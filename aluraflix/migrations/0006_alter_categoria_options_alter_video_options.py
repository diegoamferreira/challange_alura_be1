# Generated by Django 4.1.6 on 2023-02-05 21:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aluraflix', '0005_alter_categoria_cor'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categoria',
            options={'ordering': ['pk']},
        ),
        migrations.AlterModelOptions(
            name='video',
            options={'ordering': ['pk']},
        ),
    ]
