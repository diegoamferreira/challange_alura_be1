from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from aluraflix.views import Video


class VideosTestCase(APITestCase):

    def setUp(self):
        self.list_url = reverse('videos-list')
        self.curso_1 = Video.objects.create(
            titulo='VD1', descricao='Video teste 1', url='https://www.teste.com.br/video1'
        )
        self.video2 = Video.objects.create(
            titulo='VD2', descricao='Video teste 2', url='https://www.teste.com.br/video2'
        )

    def test_requisicao_get_para_listar_videos(self):
        """Teste para verificar a requisição GET para listar os cursos"""
        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
