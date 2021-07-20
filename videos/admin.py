from django.contrib import admin
from videos.models import Video


class Videos(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'descricao')
    list_display_links = ('id', 'titulo', 'descricao')
    search_fields = ('descricao',)
    list_filter = ('descricao',)
    list_per_page = 25


admin.site.register(Video, Videos)
