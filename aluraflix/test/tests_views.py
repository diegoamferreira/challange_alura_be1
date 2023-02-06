from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from aluraflix.models import Categoria
from aluraflix.views import Video


class VideoViewSetTestCase(APITestCase):

    def setUp(self):
        self.list_url = reverse('videos-list')
        self.categoria = Categoria.objects.create(
            titulo='Programação',
            cor='#CCC'
        )
        self.video1 = Video.objects.create(
            titulo='VD1', descricao='Video teste 1', url='https://www.teste.com.br/video1', categoria_id=1
        )
        self.video2 = Video.objects.create(
            titulo='VD2', descricao='Video teste 2', url='https://www.teste.com.br/video2', categoria_id=1
        )

    def test_requisicao_get_para_listar_videos(self):
        """Teste para verificar a requisição GET para listar os videos"""
        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_requisicao_post_para_criar_video(self):
        """Teste para verificar a requisição POST para criar um video"""
        data = {
            'titulo': 'Video teste 3',
            'descricao': 'Video teste 3 desc',
            'url': 'https://www.teste.com.br/video2',
            'categoria': 1
        }
        response = self.client.post(self.list_url, data=data)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

    def test_requisicao_delete_para_deletar_video(self):
        """Teste para verificar a requisição DELETE para deletar um video"""
        response = self.client.delete('/videos/1/')
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_requisicao_put_para_atualizar_video(self):
        """Teste para verificar a requisição PUT para atualizar um video"""
        data = {
            'titulo': 'Video novo nome teste 333',
            'descricao': 'Video nova desc 333',
            'url': 'https://www.teste.com.br/video333',
            'categoria': 1
        }
        response = self.client.put('/videos/1/', data=data)
        self.assertEquals(response.status_code, status.HTTP_200_OK)


class CategoriaViewSetTestCase(APITestCase):

    def setUp(self):
        self.list_url = reverse('categorias-list')
        self.categoria1 = Categoria.objects.create(
            titulo='Programação',
            cor='#CCC'
        )
        self.categoria2 = Categoria.objects.create(
            titulo='Liderança',
            cor='#FFF'
        )
        self.video1 = Video.objects.create(
            titulo='VD1', descricao='Video teste 1', url='https://www.teste.com.br/video1', categoria_id=1
        )
        self.video2 = Video.objects.create(
            titulo='VD2', descricao='Video teste 2', url='https://www.teste.com.br/video2', categoria_id=2
        )

    def test_requisicao_get_para_listar_categoria(self):
        """Teste para verificar a requisição GET para listar as categorias"""
        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_requisicao_post_para_criar_categoria(self):
        """Teste para verificar a requisição POST para criar uma categoria"""
        data = {
            'titulo': 'Categoria teste 1',
            'cor': '#154826',
        }
        response = self.client.post(self.list_url, data=data)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

    def test_requisicao_delete_para_deletar_categoria(self):
        """Teste para verificar a requisição DELETE para deletar uma categoria"""
        response = self.client.delete('/categorias/1/')
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_requisicao_put_para_atualizar_categoria(self):
        """Teste para verificar a requisição PUT para atualizar uma categoria"""
        data = {
            'titulo': 'Categoria novo teste 1',
            'cor': '#563445',
        }
        response = self.client.put('/categorias/1/', data=data)
        self.assertEquals(response.status_code, status.HTTP_200_OK)


class CategoriaVideosViewSetTestCase(APITestCase):

    def setUp(self):
        self.categoria1 = Categoria.objects.create(
            titulo='Programação',
            cor='#CCC'
        )
        self.categoria2 = Categoria.objects.create(
            titulo='Programação v2',
            cor='#FFF'
        )
        self.video1 = Video.objects.create(
            titulo='VD1', descricao='Video teste 1', url='https://www.teste.com.br/video1', categoria=self.categoria1
        )
        self.video2 = Video.objects.create(
            titulo='VD2', descricao='Video teste 2', url='https://www.teste.com.br/video2', categoria=self.categoria1
        )
        self.video3 = Video.objects.create(
            titulo='VD3', descricao='Video teste 3', url='https://www.teste.com.br/video3', categoria=self.categoria2
        )
        self.list_url = reverse('videos_categoria_list', kwargs={'pk': self.categoria1.pk})

    def test_requisicao_get_para_listar_videos_categoria(self):
        """Teste para verificar a requisição GET para listar as categorias"""
        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_requisicao_get_para_listar_videos_quantidade_correta(self):
        """Teste para verificar a requisição GET para listar somente os videos de uma determinada categoria"""
        response = self.client.get(self.list_url)
        json_response = response.json()
        self.assertEquals(len(json_response), 2)
