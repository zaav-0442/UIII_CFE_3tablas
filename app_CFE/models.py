from django.db import models

# ==========================================
# MODELO: SUCURSAL
# ==========================================
class Sucursal(models.Model):
    nombre = models.CharField(max_length=100)
    clave = models.CharField(max_length=50)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)
    ciudad = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    fecha_apertura = models.DateField()

    def __str__(self):
        return self.nombre


# ==========================================
# MODELO: EMPLEADO
# ==========================================
class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    puesto = models.CharField(max_length=100)
    rfc = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    fecha_contratacion = models.DateField()
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE, related_name="empleados")

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


# ==========================================
# MODELO: DOMICILIO
# ==========================================
class Domicilio(models.Model):
    calle = models.CharField(max_length=100)
    numero = models.CharField(max_length=10)
    colonia = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    codigo_postal = models.CharField(max_length=10)
    titular = models.CharField(max_length=100)
    fecha_registro = models.DateField()
    empleados_asignados = models.ManyToManyField(Empleado, related_name="domicilios")

    def __str__(self):
        return f"{self.calle} #{self.numero}"

