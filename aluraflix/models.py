from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


class Video(models.Model):
    titulo = models.CharField('Título', max_length=30)
    descricao = models.TextField('Descrição')
    url = models.URLField('URL')
    categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE, default=1)

    class Meta:
        ordering = ['pk']

    def __str__(self):
        return self.titulo


class Categoria(models.Model):
    titulo = models.CharField('Titulo', max_length=30)
    cor = models.CharField('Cor', max_length=7, unique=True, validators=[
        RegexValidator(
            regex=r'^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$',
            message=_('A Cor precisa estar em código Hexadecimal (#FFFFFF | #FFF)'),
        ),
    ])

    class Meta:
        ordering = ['pk']

    def __str__(self):
        return self.titulo
