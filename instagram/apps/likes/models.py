from django.db import models

# Create your models here.

class Like(models.Model):
	usuario_id = models.IntegerField()
	pblicacion_id = models.IntegerField()

		