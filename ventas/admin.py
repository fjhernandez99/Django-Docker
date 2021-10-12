from django.contrib import admin
from ventas.models import Producto, Venta, DetalleVenta
# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    fieldsets = ( 
    ('Detalles del producto:', {'fields': ('categoria', 'nombre', 'precio', 'description', 'inventario' ,)}),
    )
    list_display = ('nombre', 'categoria', 'precio', 'inventario')

class DetalleInLine(admin.TabularInline):
    model = DetalleVenta
    extra = 1

class VentaAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'total', 'forma_pago', 'recepcion', 'entrega')
    inlines = [DetalleInLine]

admin.site.register(Producto, ProductoAdmin)
admin.site.register(Venta, VentaAdmin)