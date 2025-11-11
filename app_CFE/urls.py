from django.urls import path
from . import views

urlpatterns = [
    # =============================
    # INICIO
    # =============================
    path('', views.inicio_cfe, name='inicio_cfe'),

    # =============================
    # SUCURSALES
    # =============================
    path('sucursales/', views.ver_sucursales, name='ver_sucursales'),
    path('sucursales/agregar/', views.agregar_sucursal, name='agregar_sucursal'),
    path('sucursales/actualizar/<int:id>/', views.actualizar_sucursal, name='actualizar_sucursal'),
    path('sucursales/borrar/<int:id>/', views.borrar_sucursal, name='borrar_sucursal'),

    # =============================
    # EMPLEADOS
    # =============================
    path('empleados/', views.ver_empleados, name='ver_empleados'),
    path('empleados/agregar/', views.agregar_empleado, name='agregar_empleado'),
    path('empleados/actualizar/<int:id>/', views.actualizar_empleado, name='actualizar_empleado'),
    path('empleados/borrar/<int:id>/', views.borrar_empleado, name='borrar_empleado'),

    # =============================
    # DOMICILIOS
    # =============================
    path('domicilios/', views.ver_domicilios, name='ver_domicilios'),
    path('domicilios/agregar/', views.agregar_domicilio, name='agregar_domicilio'),
    path('domicilios/actualizar/<int:id>/', views.actualizar_domicilio, name='actualizar_domicilio'),
    path('domicilios/borrar/<int:id>/', views.borrar_domicilio, name='borrar_domicilio'),
]
