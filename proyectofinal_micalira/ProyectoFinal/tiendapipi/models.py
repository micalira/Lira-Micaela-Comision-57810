from django.db import models
from django.contrib.auth.models import User

# Modelo de negocio de la aplicacion para la tercer pre entrega para mi emprendimiento de venta de termos TiendaPipi

class TiendaMinorista(models.Model):
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    telefono = models.CharField(max_length=60)
    dni = models.CharField(max_length=60)
    email = models.EmailField()
    
class TiendaMayorista(models.Model):
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    telefono = models.CharField(max_length=60)
    dni = models.CharField(max_length=60)
    email = models.EmailField()
     
class ProductosMinorista(models.Model):
    nombre = models.CharField(max_length=60)
    valor = models.CharField(max_length=60)
    cantidad = models.CharField(max_length=60)
    tamaño = models.CharField(max_length=60)
    peso = models.CharField(max_length=60)

class ProductosMayorista(models.Model):
    nombre = models.CharField(max_length=60)
    valor = models.CharField(max_length=60)
    cantidad = models.CharField(max_length=60)
    tamaño = models.CharField(max_length=60)
    peso = models.CharField(max_length=60)
    
class ProveedorMercaderia(models.Model) :
    nombre = models. CharField(max_length=60)
    pagina = models.CharField(max_length=60)
    email = models.EmailField()
    costoenvio = models.CharField(max_length=50)
    demoraenvio = models.CharField(max_length=50)
    
class EmpresaEnvioClientes(models.Model) :
    nombre = models. CharField(max_length=60)
    pagina = models.URLField()
    email = models.EmailField() 
    costoenvio = models.CharField(max_length=50)
    demoraenvio = models.CharField(max_length=50)

class EntregableProducto(models.Model):
    nombre = models.CharField(max_length=50)
    provincia = models.CharField(max_length=60)
    empresaenvio = models.CharField(max_length=60)
    fechaEntrega = models.DateField()
    entregado = models.BooleanField()
    
class Avatar(models.Model):   
    imagen = models.ImageField(upload_to="avatares") 
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} {self.imagen}"    