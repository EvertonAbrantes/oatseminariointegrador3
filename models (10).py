from django.db import models

# Create your models here.

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.CharField(max_length=3)
    genero = models.CharField(max_length=1)
    cpf = models.CharField(max_length=11)
    endereco = models.CharField(max_length=100)
    telefone= models.CharField(max_length=11)