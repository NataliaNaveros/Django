from django.db import models
from usuarios.models import Usuario

# Create your models here.

class Publicacion(models.Model):
	usuario_id = models.ForeignKey(Usuario, on_delete=models.CASCADE)
	foto = models.ImageField(upload_to='publicacion/fotos')
	descripcion = models.TextField()
	crear = models.DateTimeField(auto_now_add = True)
	actualizar = models.DateTimeField(auto_now = True)

		