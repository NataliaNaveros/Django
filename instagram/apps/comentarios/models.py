from django.db import models

# Create your models here.

class Comentario(models.Model):
	usuario_id = models.IntegerField()
	publicacion_id = models.IntegerField()
	contenido = models.TextField()
	crear = models.DateTimeField(auto_now_add = True)
	actualizar = models.DateTimeField(auto_now = True)
		