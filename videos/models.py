from django.db import models


class Video(models.Model):
    titulo = models.CharField(max_length=100, blank=False)
    descricao = models.CharField(max_length=100, blank=False)
    url = models.URLField(blank=False, max_length=150, )

    def __str__(self):
        return self.titulo
