from rest_framework.viewsets import ModelViewSet
from perfil.serializers import PerfilCreateSerializer, PerfilSerializer 
from perfil.models import Perfil
from .service import PerfilService
from rest_framework.response import Response
from rest_framework import status

class PerfilViewSet(ModelViewSet):
    service_class = PerfilService()
    serializer_class = PerfilSerializer
    queryset = Perfil.objects.all()
    http_method_names = ["get", "post", "patch"]

    def create(self, request, *args, **kwargs):
        serializer = PerfilCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = self.service_class.busca_cep(request.data.get('cep'))
        if data is None:
            return Response ({"message": "Erro para buscar o cep"}, status=status.HTTP_201_CREATED, headers=headers)
        data = self.service_class.create_to_save(data, request.data)
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)