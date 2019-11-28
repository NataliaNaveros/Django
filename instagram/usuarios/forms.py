from django import forms 

from django.contrib.auth.models import User
from usuarios.models import Perfil

class ProfileForm(forms.Form):
	website = forms.URLField(max_length=200, required=True)
	biografia = forms.CharField(max_length=500, required=False)
	telefono = forms.CharField(max_length=20, required=False)
	foto = forms.ImageField()