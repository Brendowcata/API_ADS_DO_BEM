from rest_framework.viewsets import ModelViewSet
from perfil.serializers import PerfilSerializer 
from perfil.models import Perfil 
import service

class PerfilViewSet(ModelViewSet):
    serializer_class = PerfilSerializer
    queryset = Perfil.objects.all()
    http_method_names = ["get", "post", "patch"]

    def create(self, request, *args, **kwargs):
        endereco = service.busca_cep(request.data.get("cep"))
        return super().create(request, *args, **kwargs)