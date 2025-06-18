from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

class MilitarUser(AbstractUser):
    TIPO_CHOICES = (
        ('aluno', 'Aluno'),
        ('admin', 'Administrador'),
    )
    
    matricula = models.CharField(max_length=20, unique=True)
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES, default='aluno')
    nome_completo = models.CharField(max_length=100)
    
    USERNAME_FIELD = 'matricula'
    REQUIRED_FIELDS = ['nome_completo']
    
    def __str__(self):
        return f"{self.nome_completo} ({self.matricula})"