from django.db import models
from usuarios.models import Usuario
from publicaciones.models import Publicacion


# Create your models here.

class Comentario(models.Model):
	usuario_id = models.ForeignKey(Usuario, on_delete=models.CASCADE)
	publicacion_id = models.ForeignKey(Publicacion, on_delete=models.CASCADE)
	contenido = models.TextField()
	crear = models.DateTimeField(auto_now_add = True)
	actualizar = models.DateTimeField(auto_now = True)
		