from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponseRedirect
from django.db.utils import IntegrityError
from django.contrib.auth.models import User
from usuarios.models import Usuario

# Create your views here.
def usuario(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user:
			login(request, user)
			return redirect('publicaciones')
		else:
			return render(request, 'usuarios/login.html', {'error' : 'Credenciales invalidas'})
	return render(request, 'usuarios/login.html')

@login_required()
def logout_view(request):
	logout(request)
	return redirect('login')


def registro(request):
	
	if request.method == 'POST':

	 	username = request.POST['username']
	 	password = request.POST['password']
	 	password_confirmation = request.POST['password_confirmation']

	 	if password != password_confirmation:
	 		return render(request, 'usuarios/register.html', {'error' : 'Las contraseñas no coinciden'})
	 	try:
	 		usuario = User.objects.create_user(username=username, password=password)
	 	except IntegrityError:
	 		return render(request, 'usuarios/register.html', {'error' : 'El usuario ya existe'})

	 	usuario.first_name = request.POST['first_name']
	 	usuario.last_name = request.POST['last_name']
	 	usuario.email = request.POST['email']
	 	usuario.save()

	 	profile = Usuario(user=usuario)
	 	profile.save()

	 	return redirect('login')

	return render(request, 'usuarios/register.html')
