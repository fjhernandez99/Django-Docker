"""prueba_usuario URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from usuarios.views import form_photo, user, products, customer, registroadmin, log, lognt, form_photo, bloqueo, change_password, change_user
from django.conf import settings
from django.conf.urls.static import static
from interfaz.views import accesorios, home, registrocliente, ubicaciones, productos, consolas, accesorios, juegos, membresias
from reportes.views import pdfattempts, pdflogin, pdfinventario

urlpatterns = [
    path('login/', log),
    path('admin/', admin.site.urls),
    path('user/', user),
    path('registro-admin/', registroadmin),
    path('logout/', lognt),
    path('products/', products),
    path('error/', bloqueo),
    path('home/', home),
    path('', home),
    path('registrarse/', registrocliente),
    path('password/', change_password),    
    path('change-password/', change_password),
    path('change-profile/', change_user),
    path('reporte-login/', pdflogin),
    path('reporte-intentos/', pdfattempts),
    path('reporte-inventario/', pdfinventario),
    path('ubicaciones/', ubicaciones),
    path('productos/', productos),
    path('productos/consolas/', consolas),
    path('productos/accesorios/', accesorios),
    path('productos/juegos/', juegos),
    path('productos/membresias/', membresias),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
