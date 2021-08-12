from django.db.models.query import QuerySet
#importa filters
from rest_framework import serializers, viewsets, filters, generics
from rest_framework import authentication
from rest_framework import permissions
from videos.serializers import VideoSerializer, CategoriaSerializer, VideosPorCategoriaSerializer
from videos.models import Video, Categoria
#pip install django-filter
from django_filters.rest_framework import DjangoFilterBackend, filterset

from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class VideosViewSet(viewsets.ModelViewSet):
    """Listando todos os vídeos"""
    #reverse()
    queryset = Video.objects.order_by('id').all()
    serializer_class = VideoSerializer
    #Configurando o filter
    filter_backends = [DjangoFilterBackend,
                       filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['titulo']
    search_fields = ['titulo']
    #filterset_fields = ['ativo']
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class VideosFreeViewSet(generics.ListAPIView):
    """Listando 2 vídeos"""
    #reverse()
    queryset = Video.objects.order_by('id').all().reverse()[:2]
    serializer_class = VideoSerializer


class CategoriasViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.order_by('titulo').all()
    serializer_class = CategoriaSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class VideosPorCategoriaViewSet(generics.ListAPIView):
    def get_queryset(self):
        queryset = Video.objects.order_by('id').filter(
            categoria_id=self.kwargs['pk'])
        return queryset
    serializer_class = VideosPorCategoriaSerializer
    authentication_classes = [BasicAuthentication]
    permissions_classes = [IsAuthenticated]
