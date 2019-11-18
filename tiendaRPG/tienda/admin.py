from django.contrib import admin
from . import models as m
# Register your models here.

class ProductosAdmin(admin.ModelAdmin):
    list_display = ('nombreProducto','codigo_producto','precio','puntos','descripcion','stock')

class PerfilesAdmin(admin.ModelAdmin):
    list_display = ('usuario','victorias','derrotas','total_puntos')

admin.site.register(m.Perfil,PerfilesAdmin),
admin.site.register(m.Recompensa),
admin.site.register(m.Clase_Personaje),
admin.site.register(m.Accesorio),
admin.site.register(m.carro),
admin.site.register(m.CarroProducto),
admin.site.register(m.Productos,ProductosAdmin)