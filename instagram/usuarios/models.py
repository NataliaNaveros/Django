from django.db import models
from datetime import datetime
# Create your models here.

class usuarios(models.Model):
	usuario = models.CharField(max_length=255)
	contrasena = models.CharField(max_length=255)
	correo = models.CharField(max_length=255)
	nombre_completo = models.CharField(max_length=255)
	imagen_perfil = models.ImageField(upload_to='static/images/perfil', blank=True, null=True)
	fecha_creacion = models.DateTimeField(auto_now_add=True)
	class Meta:
		verbose_name = "Usuario"
		verbose_name_plural = "Usuarios"
	def __str__(self):
		return '{}'.format(self.nombre_completo)
		