from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Usuario(models.Model):
	user=models.OneToOneField(User, on_delete=models.CASCADE)
	nombre = models.CharField(max_length=50)
	apellido = models.CharField(max_length=50)
	usuario = models.CharField(max_length=50, unique = True)
	email = models.EmailField()
	contrasena = models.CharField(max_length=50)
		