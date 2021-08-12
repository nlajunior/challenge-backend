from django.contrib import admin
from django.db import router
from django.urls import path, include
from rest_framework import routers
from videos.views import VideosViewSet, CategoriasViewSet, VideosPorCategoriaViewSet, VideosFreeViewSet


router = routers.DefaultRouter()
router.register('videos', VideosViewSet, basename='Videos')
router.register('categorias', CategoriasViewSet, basename='Categorias')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('categorias/<int:pk>/videos/', VideosPorCategoriaViewSet.as_view()),
    path('videos/free', VideosFreeViewSet.as_view())
]
