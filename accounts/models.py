from django.db import models
from django.contrib.auth.models import User


class account(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=25)

class perfil(models.Model):
    telefone = models.CharField(max_length=16, null=True)
    cpf = models.CharField(max_length=14, null=True)
    cidade = models.CharField(max_length=50, null=True)
    usuario = models.OneToOneField(User, on_delete=models.PROTECT)