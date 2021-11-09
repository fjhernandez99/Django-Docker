from django.shortcuts import render, get_object_or_404
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from usuarios.models import Usuario
from ventas.models import Producto, Carrito, Venta
from ventas.forms import ProductoForm, CarritoForm
from django.views.generic import ListView
from datetime import datetime, timedelta
from django.db.models import Sum, F
import re
# Create your views here.


def Listar(request):
    productoslistados = Producto.objects.all() 
    #Esto es un diccionario que sirve para enviar lo que se necesita para el HTML
    #Return cuando no se usa diccionario:
    #return render(request, "gestionCursos.html", {"cursos": cursoslistados})    

    #Return que se usa con el diccionario:
    return render(request, "ventas/lista-productos.html", {"productos": productoslistados})
    #return HttpResponse("<h1> Hola Mundo </h1>")

def eliminar_productos(request,id):
    productoslistados= Producto.objects.get(id=id)
    productoslistados.delete()

    return redirect('/registrar-producto') #Redirecciona a la ruta principal


class ProductosListView(ListView):
    model = Producto
    template_name = 'ventas/lista-productos.html'

    #Tambien la sobreescritura con filtros se puede usar como
    #La siguiente definicion solo muestra los menores a 4
    #def get_queryset(self):
    #    return Curso.objects.filter(creditos__lte=4)

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['titulo'] = 'Gestion de Cursos'
        return context


def agregar_carrito(request, id, username):
    productos= Producto.objects.get(id=id)
    cliente = Usuario.objects.get(username=username)
    compra = Carrito.objects.create(cliente=cliente.username, photo = productos.photo, producto = productos.nombre, precio=productos.precio)
    compra.save();
    print("Usuario registrado")
    return redirect('/carrito')

class CarritoListView(ListView):
    model = Carrito
    template_name = 'interfaz/carrito.html'

    #Tambien la sobreescritura con filtros se puede usar como
    #La siguiente definicion solo muestra los menores a 4
    #def get_queryset(self):
    #    return Curso.objects.filter(creditos__lte=4)

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['titulo'] = 'Gestion de Cursos'
        return context

def Listarcarrito(request):
    if Carrito.objects.all().count() != 0:
        total = str(Carrito.objects.all().aggregate(Sum(F('precio'))))
        total_carrito = re.findall("\d+\.\d+",total)
        tot = total_carrito[0]
    else:
        tot = format(0.00, '.2f')

    #print(total_carrito[0])
    productoslistados = Carrito.objects.all() #(usuarioOrden__startswith=username)

    return render(request, "interfaz/carrito.html", {"total_carrito": tot, "carrito": productoslistados})

def eliminar_carrito(request,id):
    productoslistados= Carrito.objects.get(id=id)
    productoslistados.delete()

    return redirect('/carrito') #Redirecciona a la ruta principal


def registrar_producto(request):
    context = {}
    if request.method == 'POST':
        nombre = request.POST['txtNombreP']
        precio = request.POST['numPrecio']
        inventario_pradera = request.POST['inv_pradera']
        inventario_roosevelt = request.POST['inv_peri']
        categoria = request.POST['txtCategoria']
        description = request.POST['descripcion']
        compañia = request.POST['compañia']
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.cleaned_data.get("photo")
        if Producto.objects.filter(nombre=nombre).exists():
            messages.info(request, 'El nombre del producto ya existe.')
            return redirect('/')
        else:
            user = Producto.objects.create(nombre=nombre, compañia=compañia, precio=precio, inventario_pradera=inventario_pradera, inventario_roosevelt=inventario_roosevelt, description=description, categoria=categoria, photo=photo)
            user.save();
            print("Usuario registrado")
            messages.info(request, 'El producto fue registrado exitosamente.')
            return redirect('/registrar-producto')
    else:
        context['form'] = ProductoForm()
        return render(request, "ventas/registrarproducto.html", context)

def checkout(request):
    total = str(Carrito.objects.all().aggregate(Sum(F('precio'))))
    total_carrito = re.findall("\d+\.\d+",total)
    entrega = datetime.now()+timedelta(days=3)
    productoslistados = Carrito.objects.all()
    if request.method == 'POST':
        cliente = request.POST['cliente']
        nit = request.POST['nit']
        direccion = request.POST['direccion']
        forma_pago = request.POST['pago']
        sucursal = request.POST['sucursal']
        venta = Venta.objects.create(cliente=cliente, vendedor = "online", nit=nit, direccion=direccion, forma_pago=forma_pago, sucursal=sucursal, total=total_carrito[0], entrega=entrega)
        venta.save();
        productoslistados=Carrito.objects.all().delete()
        context = {}
        print("Usuario registrado")
        messages.info(request, 'El checkout fue realizado exitosamente.')
        return render(request, 'ventas/checkout.html', context)
        #return redirect('/checkout')
    else:
        return render(request, "ventas/checkout.html", {"total_carrito":total_carrito[0], "carrito": productoslistados, "entrega": entrega})
