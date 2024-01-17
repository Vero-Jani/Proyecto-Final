from django.contrib import admin
from .models import Circuito, Dependencia, Distrito, Informe, Mantenimiento, Personal, ReclamoSugerencia, Rol, Solicitud, Subcircuito, Usuario, Vehiculo

# Registro los models
admin.site.register(Circuito)
admin.site.register(Dependencia)
admin.site.register(Distrito)
admin.site.register(Informe)
admin.site.register(Mantenimiento)
admin.site.register(Personal)
admin.site.register(ReclamoSugerencia)  # Nuevo modelo agregado
admin.site.register(Rol)
admin.site.register(Solicitud)
admin.site.register(Subcircuito)
admin.site.register(Usuario)
admin.site.register(Vehiculo)
# Register your models here.
