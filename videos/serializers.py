from typing import SupportsRound
from django.db import models
from django.db.models import fields
from rest_framework import serializers
from videos.models import Video, Categoria
from videos.validators import *


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

    def validate(self, data):
        if not titulo_valido(data['titulo']):
            raise serializers.ValidationError({'Titulo':"O campo titulo deve conter apenas letras."})
        return data
       

class VideoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Video
        fields = '__all__'
        #fields = ['id', 'titulo', 'descricao', 'url', 'categoria_id']
        #exclude =[]    

class VideosPorCategoriaSerializer(serializers.ModelSerializer):
    categoria_titulo = serializers.ReadOnlyField(source='categoria.titulo')
    #categoria = serializers.SerializerMethodField()
    class Meta:
        model= Video
        fields= ['titulo','url', 'descricao','categoria_id', 'categoria_titulo']

    #def get_categoria(self, obj):
    #    return obj.get_categoria_display()