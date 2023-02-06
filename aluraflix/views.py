from rest_framework import viewsets, generics, filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated

from aluraflix.models import Video, Categoria
from aluraflix.serializers import VideoSerializer, CategoriaSerializer


class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['titulo']


class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class CategoriaVideosViewSet(generics.ListAPIView):
    # queryset = Video.objects.all()
    serializer_class = VideoSerializer

    def get_queryset(self):
        queryset = Video.objects.filter(categoria=self.kwargs['id'])
        return queryset


class VideosFreeViewSet(generics.ListAPIView):
    queryset = Video.objects.all().reverse()[:10]
    serializer_class = VideoSerializer
    permission_classes = (AllowAny,)
    authentication_classes = (TokenAuthentication,)
