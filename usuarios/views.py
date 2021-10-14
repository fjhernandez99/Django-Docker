from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from usuarios.forms import UsuariosForm
from usuarios.models import Usuario
from django.contrib.auth import authenticate, login, logout
from usuarios.forms import UsuariosForm

# Create your views here.
def user(request):
    return render(request, 'usuarios/dashboard.html')

def registroadmin(request):
    context = {}
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        age = request.POST['age']
        password = request.POST['password']
        role = request.POST['role']
        form = UsuariosForm(request.POST, request.FILES)
        if form.is_valid():
                photo = form.cleaned_data.get("photo")

        if Usuario.objects.filter(username=username).exists():
            messages.info(request, 'El nombre de usuario "Username" ya existe')
            return redirect('/registro-admin')
        elif Usuario.objects.filter(email=email).exists():
            messages.info(request, 'El correo "Email" ya fue registrado anteriormente')
            return redirect('/registro-admin')
        else:
            user = Usuario.objects.create_user(username = username, password = password, email=email, first_name=first_name, last_name=last_name, age=age, role=role, photo=photo)
            user.save();
            print("Usuario registrado")
            return redirect('/user')
        


    else:
        context['form'] = UsuariosForm()
        return render(request, "usuarios/registro.html", context)


def log(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request=request,username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/user')
            print("Bienvenido")
        else:
            messages.info(request, 'El nombre de usuario "username" o contraseña están incorrectos')
            return redirect('/')
    else:
        return render(request, 'usuarios/login.html')


def lognt(request):
    logout(request)
    return redirect('/')

def form_photo(request):
    context = {}
    context['form'] = UsuariosForm()
    return render(request, "usuarios/registro.html", context)


def bloqueo(request):
    return render(request, 'usuarios/error.html')

def products(request):
    return HttpResponse('products')

def customer(request):
    return HttpResponse('customer')
