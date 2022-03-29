from rest_framework.viewsets import ModelViewSet

from Usuario.models import UsuarioModel
from Usuario.serializers import UsuarioCreateSerializer, UsuarioSerializer
from rest_framework.response import Response
from rest_framework import status
from perfil.models import Perfil

from perfil.serializers import PerfilCreateSerializer

class UsuarioViewSet(ModelViewSet):
    queryset = UsuarioModel.objects.all()
    serializer_class = UsuarioSerializer
    http_method_names = ['post', 'patch', 'get']

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object(Perfil)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


