from django.db import models
from usuarios.models import Usuario


# Create your models here.

class Seguidor(models.Model):
	seguidor_id = models.IntegerField()
	usuario_id = models.ForeignKey(Usuario, on_delete=models.CASCADE)
	validacion = models.BooleanField()
		