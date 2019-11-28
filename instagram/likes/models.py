from django.db import models
from publicaciones.models import publicaciones
from usuarios.models import usuarios 
from datetime import datetime

class likes(models.Model):
	usuario = models.ForeignKey(usuarios, on_delete=models.CASCADE)
	publicacion = models.ForeignKey(publicaciones, on_delete=models.CASCADE)

	class Meta:
		verbose_name = "Like"
		verbose_name_plural = "Likes"
	
	def __str__(self):
		return '{} dejo un me gusta a la publicacion de {}'.format(self.usuario.nombre_completo, self.publicacion.usuario.nombre_completo)

		