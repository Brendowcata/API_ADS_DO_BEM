from django.contrib import admin
from perfil.models import Perfil

class ListandoPerfil(admin.ModelAdmin):
    list_display = ('nome_instituicao', 'cnpj', 'logradouro', 'telefone', 'ano_fundacao', 'total_membros', 'nome_presidente_instituicao')
    list_display_links = ('nome_instituicao', 'cnpj')
    search_fields = ('nome_instituicao', 'cnpj', 'logradouro')
    list_filter = ('nome_instituicao', 'cnpj', 'logradouro')
    list_per_page = 10

admin.site.register(Perfil, ListandoPerfil)