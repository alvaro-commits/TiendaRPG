from django.db import models
from django.conf import settings


class Productos(models.Model):
    descuento = models.FloatField(max_length=3, default=0)
    codigo_producto = models.AutoField(primary_key=True)
    nombreProducto = models.CharField(max_length=200)
    precio = models.FloatField()
    puntos = models.FloatField()
    descripcion = models.CharField(max_length=200)
    stock = models.IntegerField()
    urlImagen = models.CharField(max_length=2083)


class CarroProducto(models.Model):
     producto = models.ForeignKey(Productos, on_delete=models.CASCADE)
     cantidad = models.IntegerField(default=1)
     def __str__(self):
         return self.producto.nombreProducto

class carro(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ManyToManyField(CarroProducto)
    realizado = models.BooleanField(default=False)
    fechaCreacion= models.DateTimeField(auto_now_add=True)
    fechaVenta= models.DateTimeField(auto_now_add=True)
    preciototal=models.FloatField(default=0)
    totalpuntos=models.FloatField(default=0)

    def __str__(self): 
        return str(self.fechaVenta)

    



class Clase_Personaje(models.Model):
    nombre = models.CharField(max_length=30)
    vida_base = models.IntegerField()
    daño_base = models.FloatField()
    defensa_base = models.FloatField()
    urlImagen = models.CharField(max_length=2083)


CATEGORIA_ACCESORIOS = (
    ('ca', 'Casco'),
    ('pe', 'Peto'),
    ('ma', 'Manoplas'),
    ('pa', 'Pantalones'),
    ('gr', 'Grebas'),
    ('an', 'Anillo')
)


class Accesorio(models.Model):
    nombre = models.CharField(max_length=50)
    tipoAccesorio = models.CharField(choices=CATEGORIA_ACCESORIOS, max_length=10)
    tier = models.IntegerField(default=0)
    vida_extra = models.IntegerField()
    daño_extra = models.FloatField()
    defensa_extra = models.FloatField()
    costo_puntos = models.IntegerField()
    urlImagen = models.CharField(max_length=2083)



class Recompensa(models.Model):
    descuento = models.FloatField(default=0)
    Producto = models.ForeignKey(Productos, on_delete=models.DO_NOTHING)



class Perfil(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    clase = models.ForeignKey(Clase_Personaje, on_delete=models.DO_NOTHING,null=True,blank=True)
    recompensa= models.ManyToManyField(Recompensa, null = True,blank = True)
    victorias = models.IntegerField(default=0)
    derrotas = models.IntegerField(default=0)
    accesorios = models.ManyToManyField(Accesorio, null = True,blank = True)
    total_puntos = models.FloatField(default=0)
    def __str__(self):
        return self.usuario.username



