from django.db import models
from usuarios.models import Usuario
# Create your models here.

PAGO_CHOICES = (
    ('Debito', 'Tarjeta de Débito'),
    ('Credito', 'Tarjeta de Crédito'),
    ('Efectivo', 'Efectivo'),
    ('Cheque', 'Cheque'),
)

CATEGORIA_CHOICES = (
    ('Consola','Consola'),
    ('Accesorio', 'Accesorio'),
    ('Juegos','Juegos'),
    ('Membresías','Membresías')
)

class Producto(models.Model):
    categoria = models.CharField(max_length=10,choices=CATEGORIA_CHOICES, default='Consolas')
    compañia = models.CharField(max_length=50, default="")
    nombre = models.CharField(max_length=50, default="")
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField(null=True, blank=True)
    inventario_pradera = models.PositiveIntegerField(default=0)
    inventario_roosevelt = models.PositiveIntegerField(default=0)
    photo = models.ImageField(default='images/deafualt1.png')

    def __str__(self):
        return f'{self.nombre}'

class ProductoVenta(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default = 1)
    precio = models.DecimalField(max_digits=6, decimal_places=2, default = 0)

class Carrito(models.Model):
    cliente = models.CharField(max_length=50, default="")
    producto = models.CharField(max_length=50, default="")
    cantidad = models.PositiveIntegerField(default = 1)
    total = models.PositiveIntegerField(default = 1)
    precio = models.DecimalField(max_digits=6, decimal_places=2, default = 0)
    photo = models.ImageField(default='images/deafualt1.png')

    def __str__(self):
        return f'{self.cliente}'

class Venta(models.Model):
    cliente = models.CharField(max_length=50, default="")
    nit = models.CharField(max_length=10, default="")
    direccion = models.CharField(max_length=50, default="")
    sucursal = models.CharField(max_length=50, default="")
    vendedor = models.CharField(max_length=50, default="")
    total = models.DecimalField(max_digits=6, decimal_places=2)
    forma_pago = models.CharField(max_length=10,choices=PAGO_CHOICES, default='efectivo')
    recepcion = models.DateTimeField(auto_now_add=True)
    entrega = models.DateTimeField()

    def productos_carrito(self):
        return self.productos.all()


class DetalleVenta(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default = "")
