from django.db.models.query import QuerySet
from rest_framework import serializers, viewsets, filters, generics
from videos.serializers import VideoSerializer, CategoriaSerializer, VideosPorCategoriaSerializer
from videos.models import Video, Categoria
from django_filters.rest_framework import DjangoFilterBackend, filterset


class VideosViewSet(viewsets.ModelViewSet):
    """Listando todos os vídeos"""
    #reverse()
    queryset = Video.objects.order_by('id').all()
    serializer_class = VideoSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['titulo']
    search_fields = ['titulo', 'id']
    #filterset_fields = ['ativo']

class CategoriasViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.order_by('titulo').all()
    serializer_class = CategoriaSerializer
    
class VideosPorCategoriaViewSet(generics.ListAPIView):
    def get_queryset(self):
        queryset= Video.objects.order_by('id').filter(categoria_id=self.kwargs['pk'])
        return queryset
    serializer_class = VideosPorCategoriaSerializer

