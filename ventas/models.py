from django.db import models
from usuarios.models import Usuario
# Create your models here.

PAGO_CHOICES = (
    ('debito', 'Tarjeta de Débito'),
    ('credito', 'Tarjeta de Crédito'),
    ('efectivo', 'Efectivo'),
    ('cheque', 'Cheque'),
)

CATEGORIA_CHOICES = (
    ('consolas', 'Consolas'),
    ('accesorios', 'Accesorios'),
    ('juegos', 'Juegos'),
    ('membresias', 'Membresías'),
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

class Venta(models.Model):
    cliente = models.CharField(max_length=50, default="")
    total = models.DecimalField(max_digits=6, decimal_places=2)
    forma_pago = models.CharField(max_length=10,choices=PAGO_CHOICES, default='efectivo')
    cobro = models.DecimalField(max_digits=6, decimal_places=2)
    vuelto = models.DecimalField(max_digits=6, decimal_places=2)
    recepcion = models.DateTimeField()
    entrega = models.DateTimeField()
    #productos = models.ManyToManyField(Producto, through='DetalleVenta')

class DetalleVenta(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default = "")
