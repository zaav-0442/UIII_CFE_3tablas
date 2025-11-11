from django.shortcuts import render, redirect, get_object_or_404
from .models import Sucursal, Empleado, Domicilio
# =============================
# INICIO
# =============================
def inicio_cfe(request):
    return render(request, 'inicio.html')

# =============================
# CRUD: SUCURSAL
# =============================
def agregar_sucursal(request):
    if request.method == 'POST':
        Sucursal.objects.create(
            nombre=request.POST['nombre'],
            clave=request.POST['clave'],
            direccion=request.POST['direccion'],
            telefono=request.POST['telefono'],
            ciudad=request.POST['ciudad'],
            estado=request.POST['estado'],
            fecha_apertura=request.POST['fecha_apertura']
        )
        return redirect('ver_sucursales')
    return render(request, 'sucursal/agregar_sucursal.html')


def ver_sucursales(request):
    sucursales = Sucursal.objects.all()
    return render(request, 'sucursal/ver_sucursales.html', {'sucursales': sucursales})


def actualizar_sucursal(request, id):
    sucursal = get_object_or_404(Sucursal, id=id)
    if request.method == 'POST':
        sucursal.nombre = request.POST['nombre']
        sucursal.clave = request.POST['clave']
        sucursal.direccion = request.POST['direccion']
        sucursal.telefono = request.POST['telefono']
        sucursal.ciudad = request.POST['ciudad']
        sucursal.estado = request.POST['estado']
        sucursal.fecha_apertura = request.POST['fecha_apertura']
        sucursal.save()
        return redirect('ver_sucursales')
    return render(request, 'sucursal/actualizar_sucursal.html', {'sucursal': sucursal})


def borrar_sucursal(request, id):
    sucursal = get_object_or_404(Sucursal, id=id)
    sucursal.delete()
    return redirect('ver_sucursales')

# =============================
# CRUD: EMPLEADO
# =============================
def ver_empleados(request):
    empleados = Empleado.objects.all()
    return render(request, 'empleado/ver_empleados.html', {'empleados': empleados})


def agregar_empleado(request):
    sucursales = Sucursal.objects.all()
    if request.method == 'POST':
        Empleado.objects.create(
            nombre=request.POST['nombre'],
            apellido=request.POST['apellido'],
            puesto=request.POST['puesto'],
            rfc=request.POST['rfc'],
            email=request.POST['email'],
            fecha_contratacion=request.POST['fecha_contratacion'],
            salario=request.POST['salario'],
            sucursal_id=request.POST['sucursal']
        )
        return redirect('ver_empleados')
    return render(request, 'empleado/agregar_empleado.html', {'sucursales': sucursales})


def actualizar_empleado(request, id):
    empleado = get_object_or_404(Empleado, id=id)
    sucursales = Sucursal.objects.all()
    if request.method == 'POST':
        empleado.nombre = request.POST['nombre']
        empleado.apellido = request.POST['apellido']
        empleado.puesto = request.POST['puesto']
        empleado.rfc = request.POST['rfc']
        empleado.email = request.POST['email']
        empleado.fecha_contratacion = request.POST['fecha_contratacion']
        empleado.salario = request.POST['salario']
        empleado.sucursal_id = request.POST['sucursal']
        empleado.save()
        return redirect('ver_empleados')
    return render(request, 'empleado/actualizar_empleado.html', {'empleado': empleado, 'sucursales': sucursales})


def borrar_empleado(request, id):
    empleado = get_object_or_404(Empleado, id=id)
    empleado.delete()
    return redirect('ver_empleados')
# =============================
# CRUD: DOMICILIO
# =============================
def ver_domicilios(request):
    domicilios = Domicilio.objects.all()
    return render(request, 'domicilio/ver_domicilios.html', {'domicilios': domicilios})

def agregar_domicilio(request):
    empleados = Empleado.objects.all()
    if request.method == 'POST':
        calle = request.POST['calle']
        numero = request.POST['numero']
        colonia = request.POST['colonia']
        ciudad = request.POST['ciudad']
        codigo_postal = request.POST['codigo_postal']
        titular = request.POST['titular']
        fecha_registro = request.POST['fecha_registro']
        empleados_ids = request.POST.getlist('empleados')  # 👈 varios IDs

        # Crear el domicilio sin asignar todavía empleados
        domicilio = Domicilio.objects.create(
            calle=calle,
            numero=numero,
            colonia=colonia,
            ciudad=ciudad,
            codigo_postal=codigo_postal,
            titular=titular,
            fecha_registro=fecha_registro,
        )

        # Asignar los empleados seleccionados
        domicilio.empleados_asignados.set(empleados_ids)

        return redirect('ver_domicilios')

    return render(request, 'domicilio/agregar_domicilio.html', {'empleados': empleados})

def actualizar_domicilio(request, id):
    domicilio = get_object_or_404(Domicilio, id=id)
    empleados = Empleado.objects.all()

    if request.method == 'POST':
        domicilio.calle = request.POST['calle']
        domicilio.numero = request.POST['numero']
        domicilio.colonia = request.POST['colonia']
        domicilio.ciudad = request.POST['ciudad']
        domicilio.codigo_postal = request.POST['codigo_postal']
        domicilio.titular = request.POST['titular']
        domicilio.fecha_registro = request.POST['fecha_registro']
        domicilio.save()

        # ⚡ Actualizamos los empleados asignados
        empleados_ids = request.POST.getlist('empleados')
        domicilio.empleados_asignados.set(empleados_ids)

        return redirect('ver_domicilios')

    return render(request, 'domicilio/actualizar_domicilio.html', {
        'domicilio': domicilio,
        'empleados': empleados
    })

def borrar_domicilio(request, id):
    domicilio = get_object_or_404(Domicilio, id=id)
    domicilio.delete()
    return redirect('ver_domicilios')