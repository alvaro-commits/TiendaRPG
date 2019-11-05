from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
#from apps.usuario.models import usuario

class Productos(models.Model):
    descuento = models.FloatField(max_length=3)
    codigo_producto = models.IntegerField(primary_key=True)
    nombreProducto = models.CharField(max_length=200)
    precio = models.IntegerField()
    puntos = models.IntegerField()
    descripcion = models.CharField(max_length=200)
    stock = models.IntegerField()
    urlImagen = models.CharField(max_length=2083)

class Usuario(models.Model):
    usuario = models.CharField(max_length=12, primary_key=True)
    contraseña = models.CharField(max_length=15)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField()
    email = models.EmailField()
    activo = models.BooleanField(default=True)

class Carrito(models.Model):
    id_carrito = models.IntegerField(primary_key=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING)
    id_producto = models.ForeignKey(Productos, on_delete=models.DO_NOTHING)
    cantidad = models.IntegerField()
    sub_total = models.IntegerField()
    sub_puntos = models.IntegerField()


class Boleta(models.Model):
    id_boleta = models.IntegerField(primary_key=True)
    id_carrito = models.ForeignKey(Carrito, on_delete=models.DO_NOTHING)
    total = models.IntegerField()
    final_compra = models.IntegerField()


class Clase_Personaje(models.Model):
    id_clase = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=30)
    activo = models.BooleanField(default=True)
    vida_base = models.IntegerField()
    daño_base = models.FloatField()
    evasion_base = models.FloatField()


class Personaje(models.Model):
    id_personaje = models.IntegerField(primary_key=True)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING)
    id_clase = models.ForeignKey(Clase_Personaje, on_delete=models.DO_NOTHING)
    nivel = models.IntegerField()
    victorias = models.IntegerField()
    derrotas = models.IntegerField()
    urlImagen = models.CharField(max_length=2083)

class Tipo_Accesorio(models.Model): 
    id_tipo = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    daño = models.IntegerField()
    defensa = models.IntegerField()
    critico = models.IntegerField()
    velocidad = models.IntegerField()
    evasion = models.FloatField()

class Accesorio(models.Model):
    id_accesorio = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    costo_puntos = models.IntegerField()
    id_tipo = models.ForeignKey(Tipo_Accesorio, on_delete=models.DO_NOTHING)
    urlImagen = models.CharField(max_length=2083)

class Personaje_Accesorio(models.Model):
    id_personaje = models.ForeignKey(Personaje, on_delete=models.DO_NOTHING)
    id_accesorio = models.ForeignKey(Accesorio, on_delete=models.DO_NOTHING)





