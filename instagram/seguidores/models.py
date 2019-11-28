from django.db import models
from usuarios.models import usuarios
from datetime import datetime

class seguidores(models.Model):
	usuario = models.ForeignKey(usuarios, on_delete=models.CASCADE, related_name='seguidor')
	usuario_seguido = models.ForeignKey(usuarios, on_delete=models.CASCADE, related_name='seguido')

	class Meta:
		verbose_name = "Seguidor"
		verbose_name_plural = "Seguidores"
	
	def __str__(self):
		return '{} ({}) empezo a seguir a {} ({})'.format(self.usuario.nombre_completo, self.usuario.id, self.usuario_seguido.nombre_completo, self.usuario_seguido.id)