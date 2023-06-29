from django.db import models

# Create your models here.

class Arquivados(models.Model):
    numeroarquivo = models.CharField(max_length=100)
