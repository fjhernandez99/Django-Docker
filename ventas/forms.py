from django import forms

class ProductoForm(forms.Form):
    photo = forms.ImageField()

class CarritoForm(forms.Form):
    cantidad = forms.IntegerField()