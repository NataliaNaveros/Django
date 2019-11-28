from django.db import models
from usuarios.models import usuarios
from django.urls import reverse
from datetime import datetime
# Create your models here.

class publicaciones(models.Model):
	tipos =((1, "Publicacion"), (2, "Historia"),)

	usuario = models.ForeignKey(usuarios, on_delete=models.CASCADE)
	imagen = models.ImageField(upload_to='static/images/publicaciones')
	mensaje = models.TextField(blank=True)
	tipo = models.IntegerField(choices=tipos, default=1)
	fecha_creacion = models.DateTimeField(auto_now_add=True)


	class Meta:
		verbose_name = "Publicacion"
		verbose_name_plural = "Publicaciones"
	def __str__(self):
		if(self.tipo == 1):
			publicacion = 'Publicacion'
		else:
			publicacion = 'Historia'
		return '{} creada por {} a las {}'.format(publicacion, self.usuario.nombre_completo, self.fecha_creacion)
		