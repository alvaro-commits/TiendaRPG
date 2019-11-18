from django.urls import path
from tienda import views
from django.contrib.auth import views as auth_views

app_name = 'tienda'

urlpatterns = [
    path('',views.VistaMenu.as_view(), name = 'menu'),
    path('carro/',views.Vistacarro, name ='/carro'),
    
    path('perfil/',views.vistaperfil, name ='perfil'),
    path('seleccionPersonaje/',views.seleccionPersonaje, name ='seleccionPersonaje'),
    path('realizar_compra',views.realizarcompra, name ='realizarcompra'),
    path('seleccionPersonaje/(<int:id>),',views.asignarClaseAPersonaje, name ='asignarClaseAPersonaje'),
    path('añadir_al_carro/(<int:codigo_producto>),',views.añadir_al_carro, name ='añadir_al_carro'),
    path('eliminar_item_carro/(<int:item_id>),',views.eliminar_item_carro, name ='eliminar_item_carro'),
    path('registro/',views.registro, name = 'registro'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout')

]