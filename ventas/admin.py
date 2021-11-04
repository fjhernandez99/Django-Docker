from django.contrib import admin
from ventas.models import Producto, Venta, DetalleVenta
# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    fieldsets = ( 
    ('Detalles del producto:', {'fields': ('categoria', 'compañia', 'nombre', 'precio', 'description', 'inventario_pradera', 'inventario_roosevelt', 'photo')}),
    )
    list_display = ('nombre','compañia', 'categoria', 'precio', 'inventario_pradera', 'inventario_roosevelt')

class DetalleInLine(admin.TabularInline):
    model = DetalleVenta
    extra = 1

class VentaAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'total', 'forma_pago', 'recepcion', 'entrega')
    inlines = [DetalleInLine]

admin.site.register(Producto, ProductoAdmin)
admin.site.register(Venta, VentaAdmin)