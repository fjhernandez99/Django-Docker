from django import forms

class ProductoForm(forms.Form):
    photo = forms.ImageField()