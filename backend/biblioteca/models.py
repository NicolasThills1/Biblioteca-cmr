from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    TIPO_USUARIO_CHOICES = [
        ('aluno', 'Aluno'),
        ('admin', 'Administrador'),
    ]
    tipo_usuario = models.CharField(max_length=10, choices=TIPO_USUARIO_CHOICES)
    matricula = models.CharField(max_length=20, blank=True, null=True)