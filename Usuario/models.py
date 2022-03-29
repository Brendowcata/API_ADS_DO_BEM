from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import AbstractUser

from perfil.models import Perfil

class UsuarioModel(AbstractUser): #AbstractUser
    username = models.EmailField(unique=True,db_column="EMAIL")
    senha = models.CharField(max_length=20, db_column="SENHA")
    perfil = models.OneToOneField(Perfil, on_delete=models.CASCADE, null=True,db_column="PERFIL")
    
    def __str__(self):
        return self.username