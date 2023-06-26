from django.db import models

class Registros(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    telefone = models.CharField(max_length=70)

def __str__(self):
    return self.nome