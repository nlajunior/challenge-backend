from django.contrib import admin
from videos.models import Video
from videos.models import Categoria


class Videos(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'descricao')
    list_display_links = ('id', 'titulo', 'descricao')
    search_fields = ('descricao',)
    list_filter = ('descricao',)
    list_per_page = 10
    #Ordenação no Django Admin
    ordering = ('titulo',)

class Categorias(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'cor')
    list_display_links = ('id', 'titulo', 'cor')
    search_fields = ('titulo',)
    list_filter = ('titulo',)
    list_per_page = 10
    ordering = ('titulo',)


admin.site.register(Video, Videos)
admin.site.register(Categoria, Categorias)
