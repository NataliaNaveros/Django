from django import forms

from publicaciones.models import Publicacion

class PostForm(forms.ModelForm):
	class Meta:
		model = Publicacion
		fields = ('user', 'perfil', 'titulo', 'foto')