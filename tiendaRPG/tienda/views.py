from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import models as mod
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
# Create your views here.




def index(request):
    productos = mod.Productos.objects.all()
    return render(request,'index.html', 
    {'productos': productos})

@login_required
def carro(request):
    return render(request,'carro.html')


def login(request):

    return render(request,'Login.html')


def registro(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Tu cuenta ha sido creada exitosamente! ahora puedes ingresar.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request,'registro.html',{'form': form})