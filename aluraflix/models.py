from django.db import models


class Video(models.Model):
    titulo = models.CharField('Título', max_length=30)
    descricao = models.TextField('Descrição')
    url = models.URLField('URL')
