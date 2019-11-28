from django.db import models
from publicaciones.models import publicaciones
from usuarios.models import usuarios
from datetime import datetime 

class comentarios(models.Model):
	usuario = models.ForeignKey(usuarios, on_delete=models.CASCADE)
	publicacion = models.ForeignKey(publicaciones, on_delete=models.CASCADE)
	mensaje = models.TextField()
	fecha_creacion = models.DateTimeField(auto_now_add=True) 
	
	class Meta:
		verbose_name = "Comentario"
		verbose_name_plural = "Comentarios"
	
	def __str__(self):
		return 'Comentario creado por {} a las {}'.format(self.usuario.nombre_completo, self.fecha_creacion)