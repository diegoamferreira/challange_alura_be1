import os
import random
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'challange_alura_be1.settings')
django.setup()

from faker import Faker
from unidecode import unidecode

from aluraflix.models import Video, Categoria


def criando_categorias(quantidade_de_categorias):
    fake = Faker('pt_BR')
    Faker.seed(10)
    categorias_list = []
    for _ in range(quantidade_de_categorias):
        titulo = fake.job()[:30]
        c = Categoria(
            titulo=titulo,
            cor=fake.color(luminosity='light')
        )
        c.save()
        categorias_list.append(c)
    return categorias_list


def criando_videos(quantidade_de_videos, categorias_list):
    fake = Faker('pt_BR')
    Faker.seed(10)
    for _ in range(quantidade_de_videos):
        titulo = fake.first_name()[:30]
        c = Video(
            titulo=titulo,
            descricao=fake.text(),
            url=f"https://teste_url/{unidecode(titulo.lower()).replace(' ', '')}",
            categoria=random.choice(categorias_list)
        )
        c.save()


categorias_list = criando_categorias(20)
criando_videos(200, categorias_list)
