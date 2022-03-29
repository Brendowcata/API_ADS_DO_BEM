from rest_framework.viewsets import ModelViewSet

from Usuario.models import UsuarioModel
from Usuario.serializers import UsuarioSerializer

class UsuarioViewSet(ModelViewSet):
    queryset = UsuarioModel.objects.all()
    serializer_class = UsuarioSerializer
    http_method_names = ['post', 'patch', 'get']



