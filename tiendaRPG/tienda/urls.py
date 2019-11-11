from django.urls import path
from tienda import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.VistaMenu.as_view(), name = 'menu'),
    path('carro/',views.carro, name ='carro'),
    path('registro/',views.registro, name = 'registro'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout')
]