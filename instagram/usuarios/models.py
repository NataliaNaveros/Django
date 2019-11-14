from django.db import models

# Create your models here.

class Usuario(models.Model):
	nombre = models.CharField(max_length=50)
	usuario = models.CharField(max_length=50, unique = True)
	email = models.EmailField()
	contrasena = models.CharField(max_length=50)
		