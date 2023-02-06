from rest_framework import serializers

from aluraflix.models import Video, Categoria


class VideoSerializer(serializers.ModelSerializer):
    categoria = serializers.PrimaryKeyRelatedField(queryset=Categoria.objects.all())

    class Meta:
        model = Video
        fields = ['id', 'categoria', 'titulo', 'descricao', 'url']


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['titulo', 'cor']
