from django.db import models
from django.db.models.deletion import CASCADE

class Categoria(models.Model):
    titulo = models.CharField(max_length=100, blank=False, unique=True)
    cor = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return str(self.titulo)

class Video(models.Model):
    titulo = models.CharField(max_length=100, blank=False)
    descricao = models.CharField(max_length=100, blank=False)
    url = models.URLField(blank=False, max_length=150)
    categoria_id = models.ForeignKey(Categoria, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.titulo


    

