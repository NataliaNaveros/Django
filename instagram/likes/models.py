from django.db import models
from usuarios.models import Usuario
from publicaciones.models import Publicacion

# Create your models here.

class Like(models.Model):
	usuario_id = models.ForeignKey(Usuario, on_delete=models.CASCADE)
	publicacion_id = models.ForeignKey(Publicacion, on_delete=models.CASCADE)

		