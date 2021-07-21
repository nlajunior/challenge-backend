from django.contrib import admin
from django.db import router
from django.urls import path, include
from rest_framework import routers
from videos.views import VideosViewSet

router = routers.DefaultRouter()
router.register('videos', VideosViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
