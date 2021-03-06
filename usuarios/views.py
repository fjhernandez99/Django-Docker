from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from usuarios.forms import UsuariosForm
from usuarios.models import Usuario
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm, UserChangeForm
from usuarios.forms import UsuariosForm, EditarPerfilForm

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
            messages.info(request, 'El nuevo usuario ha sido registrado exitosamente')
            print("Usuario registrado")
            return redirect('/registro-admin')
        


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
            return redirect('/home')
            print("Bienvenido")
        else:
            messages.info(request, 'El nombre de usuario "username" o contrase??a est??n incorrectos')
            return redirect('/login')
    else:
        return render(request, 'usuarios/login.html')


def lognt(request):
    logout(request)
    return redirect('/home')

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

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.info(request, 'Su nueva contrase??a ha sido registrada exitosamente')
            return redirect('/change-password')
        else:
            messages.info(request, 'Hubo un error en el cambio de contrase??a, int??ntelo nuevamente')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'usuarios/contrase??a.html', {
        'form': form
    })

def change_user(request):
    if request.method == 'POST':
        form = EditarPerfilForm(request.POST, instance=request.user)
        if form.is_valid():
            user = form.save()
            messages.info(request, 'Sus cambios fueron realizados exitosamente')
            return redirect('/change-profile')
        else:
            messages.info(request, 'Hubo un error en la actualizaci??n de informaci??n, int??ntelo nuevamente')
    else:
        form = EditarPerfilForm(instance=request.user)
    return render(request, 'usuarios/perfil.html', {
        'form': form
    })