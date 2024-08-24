from django.db import models

class Filmes(models.Model):
    titulo = models.CharField(max_length=40)
    ano = models.CharField(max_length=4)
    genero = models.CharField(max_length=30)
    diretor = models.CharField(max_length=30)
