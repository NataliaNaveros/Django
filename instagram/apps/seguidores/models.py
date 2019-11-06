from django.db import models

# Create your models here.

class Seguidor(models.Model):
	seguidor_id = models.IntegerField()
	usuario_id = models.IntegerField()
	validacion = models.BooleanField()
		