from django.contrib import admin
from . import models as m
# Register your models here.

class ProductosAdmin(admin.ModelAdmin):
    list_display = ('nombreProducto','codigo_producto','precio','puntos','descripcion','stock')

admin.site.register(m.Personaje),
admin.site.register(m.Carrito),
admin.site.register(m.Productos,ProductosAdmin)