from django.test import TestCase
from . import models as mod
# Create your tests here.

class PruebaProducto(TestCase):
    def setUp(self):
        xbox = mod.Productos.objects.create(nombreProducto="Xbox one",precio=1000,puntos = 5,descripcion = 0,stock = 0, urlImagen = "imagen")
        mod.Recompensa.objects.create(descuento= 50,Producto = xbox,nuevoPrecio = 0,nivel = 5)

    def test_asignacion_precio_producto(self):
        Xbox = mod.Productos.objects.get(nombreProducto = "Xbox one")
        self.assertEqual(Xbox.precio,1000)    

    def test_asignacion_puntos_producto(self):
        Xbox = mod.Productos.objects.get(nombreProducto = "Xbox one")
        self.assertEqual(Xbox.puntos,5)    

    def test_asignacion_descuento(self):
        recompensa = mod.Recompensa.objects.get(nivel = 5)
        self.assertEqual(recompensa.obtenerNuevoPrecio(),500)   
        print(F"El nuevo precio aplicado al descuento es : "+str(recompensa.obtenerNuevoPrecio()))


