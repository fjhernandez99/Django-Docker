from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from interfaz.forms import ClienteForm
from usuarios.models import Usuario
from django.contrib.auth import authenticate, login, logout
from ventas.models import Producto, Carrito

# Create your views here.

def home(request):
    return render(request, 'interfaz/homepage.html')

def carrito(request):
    carro = Carrito.objects.all()
    context = {'carro': carro}
    return render(request, 'interfaz/carrito.html')

def consolas(request):
    productos = Producto.objects.all()
    context = {'productos': productos}
    return render(request, 'interfaz/consolas.html', context)

def accesorios(request):
    productos = Producto.objects.all()
    context = {'productos': productos}
    return render(request, 'interfaz/accesorios.html', context)

def juegos(request):
    productos = Producto.objects.all()
    context = {'productos': productos}
    return render(request, 'interfaz/juegos.html', context)

def membresias(request):
    productos = Producto.objects.all()
    context = {'productos': productos}
    return render(request, 'interfaz/membresia.html', context)

def productos(request):
    productos = Producto.objects.all()
    context = {'productos': productos}
    return render(request, 'interfaz/productos.html', context)

def registrocliente(request):
    context = {}
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        age = request.POST['age']
        password = request.POST['password']
        form = ClienteForm(request.POST, request.FILES)
        if form.is_valid():
                photo = form.cleaned_data.get("photo")

        if Usuario.objects.filter(username=username).exists():
            messages.info(request, 'El nombre de usuario "Username" ya existe')
            return redirect('/registrarse')
        elif Usuario.objects.filter(email=email).exists():
            messages.info(request, 'El correo "Email" ya fue registrado anteriormente')
            return redirect('/registrarse')
        else:
            user = Usuario.objects.create_user(username = username, password = password, email=email, first_name=first_name, last_name=last_name, age=age, role="Cliente", photo=photo)
            user.save();
            print("Usuario registrado")
            return redirect('/home')
    else:
        context['form'] = ClienteForm()
        return render(request, "interfaz/registrarse.html", context)

def ubicaciones(request):
    return render(request, 'interfaz/ubicaciones.html')