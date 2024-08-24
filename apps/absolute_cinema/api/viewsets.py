import requests
import json

from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from apps.absolute_cinema.models import Filmes
from apps.absolute_cinema.api.serializers import FilmeSerializer

class FilmesViewSet(ModelViewSet):
    queryset = Filmes.objects.all()
    serializer_class = FilmeSerializer
    
    def create(self, request, *args, **kwargs):
        titulo = request.data.get("titulo")
        
        requisicao = requests.get(
            f'https://www.omdbapi.com/?t={titulo}&apikey=6e0e1ceb'
        )
        
        requisicao_dicionario = json.loads(requisicao.content)
        
        filme_salvo = Filmes.objects.create(
            titulo=requisicao_dicionario["Title"],
            ano=requisicao_dicionario["Year"],
            genero=requisicao_dicionario["Genre"],
            diretor=requisicao_dicionario["Director"]
        )
        
        return Response(
            f'Dados do Filme - Titulo: {filme_salvo.titulo}, Diretor: {filme_salvo.diretor}, Ano: {filme_salvo.ano}, Genero: {filme_salvo.genero}', status=status.HTTP_201_CREATED
            )