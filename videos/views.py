from rest_framework import serializers, viewsets
from videos.serializers import VideoSerializer
from videos.models import Video


class VideosViewSet(viewsets.ModelViewSet):
    """Listando todos os vídeos"""
    queryset = Video.objects.order_by('id').reverse().all()
    serializer_class = VideoSerializer