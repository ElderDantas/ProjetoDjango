from rest_framework import serializers
from apps.absolute_cinema.models import Filmes

class FilmeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filmes
        fields = [
            'titulo',
            'ano',
            'genero',
            'diretor'
        ]