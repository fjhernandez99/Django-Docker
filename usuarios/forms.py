from django import forms
from usuarios.models import Usuario
from django.contrib.auth.forms import UserChangeForm

class UsuariosForm(forms.Form):
    photo = forms.ImageField()

class EditarPerfilForm(UserChangeForm):
    class Meta:
        model = Usuario
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'photo',
        )