from django.db import models
from django.conf import settings

class Productos(models.Model):
    descuento = models.FloatField(max_length=3)
    codigo_producto = models.IntegerField(primary_key=True)
    nombreProducto = models.CharField(max_length=200)
    precio = models.IntegerField()
    puntos = models.IntegerField()
    descripcion = models.CharField(max_length=200)
    stock = models.IntegerField()
    urlImagen = models.CharField(max_length=2083)


class CarroProducto(models.Model):
     producto = models.ForeignKey(Productos, on_delete=models.CASCADE)

     def __str__(self):
         return self.nombreProducto

class carro(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ManyToManyField(CarroProducto, on_delete=models.DO_NOTHING)
    realizado = models.BooleanField(default=False)
    fechaVenta= models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.usuario.username
    
    def obtenerTotal(self):
        t = 0
        for p in items:
           t = t + p.precio
        return t


class Clase_Personaje(models.Model):
    nombre = models.CharField(max_length=30)
    vida_base = models.IntegerField()
    daño_base = models.FloatField()
    defensa_base = models.FloatField()
    urlImagen = models.CharField(max_length=2083)


class Accesorio(models.Model):
    nombre = models.CharField(max_length=50)
    tipoAccesorio = models.CharField(max_length=30)
    vida_extra = models.IntegerField()
    daño_extra = models.FloatField()
    defensa_extra = models.FloatField()
    costo_puntos = models.IntegerField()
    urlImagen = models.CharField(max_length=2083)


class Personaje_Accesorio(models.Model):
    accesorio = models.ForeignKey(Accesorio, on_delete=models.DO_NOTHING)


class Personaje(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    clase = models.ForeignKey(Clase_Personaje, on_delete=models.DO_NOTHING)
    victorias = models.IntegerField()
    derrotas = models.IntegerField()
    accesorios = models.ManyToManyField(Personaje_Accesorio, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.usuario.username







