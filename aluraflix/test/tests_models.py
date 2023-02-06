from django.core.exceptions import ValidationError
from django.test import TestCase

from aluraflix.models import Video, Categoria


class VideoModelUnitTestCase(TestCase):

    def setUp(self) -> None:
        self.programa = Video(
            titulo='Django parte 1',
            descricao='descricao do video de django',
            url='https://url.video.com.br',
            categoria_id=1,
        )

    def test_verifica_atributos_do_video(self):
        """Verifica os atributos de um programa com valores default"""
        self.assertEqual(self.programa.titulo, 'Django parte 1')
        self.assertEqual(self.programa.descricao, 'descricao do video de django')
        self.assertEqual(self.programa.url, 'https://url.video.com.br')
        self.assertEqual(self.programa.categoria_id, 1)


class VideoModelIntegrationTestCase(TestCase):

    def setUp(self) -> None:
        self.categoria = Categoria.objects.create(
            titulo='Programação',
            cor='#CCC'
        )
        self.video = Video.objects.create(
            titulo='Django parte 1',
            descricao='descricao do video de django',
            url='https://url.video.com.br',
            categoria=self.categoria,
        )

    def test_verifica_atributos_do_video(self):
        """Verifica os atributos de um programa com valores default"""
        self.assertEqual(self.video.pk, 1)
        self.assertEqual(self.video.titulo, 'Django parte 1')
        self.assertEqual(self.video.descricao, 'descricao do video de django')
        self.assertEqual(self.video.url, 'https://url.video.com.br')
        self.assertEqual(self.video.categoria, self.categoria)

    def test_video_sem_descricao(self):
        """Verifica se ocorre erro ao criar um vídeo sem descrição"""
        video = Video.objects.create(
            titulo='Django parte 1',
            url='https://url.video.com.br',
            categoria=self.categoria,
        )
        try:
            video.full_clean()
        except ValidationError as e:
            self.assertTrue('descricao' in e.message_dict)

    def test_video_sem_url(self):
        """Verifica se ocorre erro ao criar um vídeo sem descrição"""
        video = Video.objects.create(
            titulo='Django parte 1',
            descricao='descricao do video de django',
            categoria=self.categoria,
        )
        try:
            video.full_clean()
        except ValidationError as e:
            self.assertTrue('url' in e.message_dict)

    def test_video_sem_categoria(self):
        """Verifica se ocorre erro ao criar um vídeo sem descrição"""
        video = Video.objects.create(
            titulo='Django parte 1',
            descricao='descricao do video de django',
            categoria=self.categoria,
        )
        try:
            video.full_clean()
        except ValidationError as e:
            self.assertTrue('url' in e.message_dict)
