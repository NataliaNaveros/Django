from django.db import models

# Create your models here.

class Publicacion(models.Model):
	usuario_id = models.IntegerField()
	foto = models.ImageField(max_length=50)
	descripcion = models.TextField()
	crear = models.DateTimeField(auto_now_add = True)
	actualizar = models.DateTimeField(auto_now = True)

		