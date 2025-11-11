from django.contrib import admin
from .models import Sucursal, Empleado, Domicilio

admin.site.register(Sucursal)
admin.site.register(Empleado)
admin.site.register(Domicilio)