from django.contrib import admin
from .models import Usuarios, Administrador, Inspector, Analista, Clientes, Areas, Equipos, Fajas, Poleas, ProcesoInspeccion, Documentos, Imagenes, PoleasProceso, FajasProceso, Parametros, Mediciones, Tabla, Filas, Columnas, Datos

# Register your models here.
admin.site.register(Usuarios)
admin.site.register(Administrador)
admin.site.register(Inspector)
admin.site.register(Analista)
admin.site.register(Clientes)
admin.site.register(Areas)
admin.site.register(Equipos)
admin.site.register(Fajas)
admin.site.register(Poleas)
admin.site.register(ProcesoInspeccion)
admin.site.register(Documentos)
admin.site.register(Imagenes)
admin.site.register(PoleasProceso)
admin.site.register(FajasProceso)
admin.site.register(Parametros)
admin.site.register(Mediciones)
admin.site.register(Tabla)
admin.site.register(Filas)
admin.site.register(Columnas)
admin.site.register(Datos)