from django.contrib import admin

# Importar las clases del modelo
from futbolec.models import *
from import_export.admin import ImportExportModelAdmin
from import_export import resources

class EquipoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('nombre', 'siglas', 'usernameTwi')
    search_fields = ('nombre', 'siglas', 'usernameTwi')
    #exclude = ("modulos",) # se excluye de la interfaz del admin


class JugadorAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('nombre', 'posicion', 'numeroCamiseta','sueldo','equipo')
    search_fields = ('nombre', 'posicion', 'numeroCamiseta','sueldo','equipo')

class CampeonatoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('nombreCampeonato','nombreAuspiciante')
    search_fields = ('nombreCampeonato','nombreAuspiciante')

class CampeonatoEquiposAdmin(ImportExportModelAdmin, admin.ModelAdmin):
	list_display = ('anio', 'equipo','campeonato')
	search_fields = ('anio', 'equipo','campeonato')

admin.site.register(Equipo, EquipoAdmin)
admin.site.register(Jugador, JugadorAdmin)
admin.site.register(Campeonato, CampeonatoAdmin)
admin.site.register(CampeonatoEquipos, CampeonatoEquiposAdmin)