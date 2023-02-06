from django.contrib import admin

from aluraflix.models import Video, Categoria


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'descricao', 'url', 'get_categoria')
    list_display_links = ('id', 'titulo')
    list_filter = ('categoria__titulo',)
    search_fields = ('titulo',)
    list_per_page = 20

    def get_categoria(self, obj):
        return obj.categoria.titulo
    get_categoria.short_description = 'Categoria'
    get_categoria.admin_order_field = 'categoria__titulo'


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'cor')
    list_display_links = ('id', 'titulo')
    search_fields = ('titulo',)
    list_per_page = 20
