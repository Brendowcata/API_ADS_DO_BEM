from django.contrib import admin

from Usuario.models import UsuarioModel

class ListandoUsuario(admin.ModelAdmin):
    list_display = ('username', 'senha')
    list_display_links = ('username', 'senha')
    search_fields = ('username',)
    list_filter = ('username',)
    list_per_page = 10

admin.site.register(UsuarioModel, ListandoUsuario)