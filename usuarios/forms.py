from django import forms

class UsuariosForm(forms.Form):
    photo = forms.ImageField()
