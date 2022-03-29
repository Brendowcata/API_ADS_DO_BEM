from dataclasses import fields
from rest_framework import serializers
from Usuario.models import UsuarioModel
from perfil.models import Perfil

class UsuarioSerializer(serializers.Serializer):
    class Meta:
        model = UsuarioModel
        exclude = ('modified', 'created')

class UsuarioPerfilSerializer(serializers.Serializer):
    class Meta:
        model = UsuarioModel
        fields = ('email', 'senha')

