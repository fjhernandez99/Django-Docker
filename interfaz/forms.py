from django import forms

class ClienteForm(forms.Form):
    photo = forms.ImageField()
