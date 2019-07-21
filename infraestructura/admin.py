from django.contrib import admin

from .models import *

admin.site.register(Referencia)
admin.site.register(Encargado)
admin.site.register(Categoria)
admin.site.register(Componente)
admin.site.register(Laboratorio)
admin.site.register(Dependencia)
admin.site.register(Programa)
admin.site.register(LaboratorioComponente)
admin.site.register(LaboratorioProgramas)
