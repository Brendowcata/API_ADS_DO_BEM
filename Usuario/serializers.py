from dataclasses import fields
from rest_framework import serializers
from Usuario.models import UsuarioModel

class UsuarioSerializer(serializers.Serializer):
    class Meta:
        model = UsuarioModel
        exclude = ('modified', 'created')

class UsuarioCreateSerializer(serializers.Serializer):
    class Meta:
        model = UsuarioModel
        fields = ('username', 'senha')

