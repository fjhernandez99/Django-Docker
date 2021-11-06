from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from ventas.models import Producto
from ventas.forms import ProductoForm
from django.views.generic import ListView
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