from django.urls import path, include
from rest_framework import routers

from aluraflix.views import VideoViewSet, CategoriaViewSet, CategoriaVideosViewSet, VideosFreeViewSet

router = routers.DefaultRouter()
router.register('videos', VideoViewSet, basename='videos')
router.register('categorias', CategoriaViewSet, basename='categorias')

urlpatterns = [
    path('videos/free/', VideosFreeViewSet.as_view(), name='videos_free_list'),
    path('categorias/<int:id>/videos/', CategoriaVideosViewSet.as_view(), name='videos_categoria_list'),
    path('', include(router.urls)),
]
