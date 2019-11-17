from django.shortcuts import render
from datetime import datetime
from django.contrib.auth.decorators import login_required


# Create your views here.

noticias = [
	{
		'titulo': 'Atardecer',
		'usuario': {
			'nombre': 'Leidy Quintero',
			'foto': 'https://picsum.photos/60/60/?image=1027',
		},
		'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
		'imagen': 'https://i.pinimg.com/originals/c4/76/27/c476278504682e622fabe9b0932098c3.jpg',
	},
	{
		'titulo': 'Peñol',
		'usuario': {
			'nombre': 'Natalia Hernandez',
			'foto': 'https://picsum.photos/60/60/?image=1005',
		},
		'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
		'imagen': 'https://uberblogapi.10upcdn.com/wp-content/uploads/2019/02/Paisajes-conquistadores-7-lugares-bonitos-en-Medell%C3%ADn-que-te-encantar%C3%A1n.png',
	},
	{
		'titulo': 'Playa',
		'usuario': {
			'nombre': 'Charles Chaplin',
			'foto': 'https://picsum.photos/60/60/?image=883',
		},
		'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
		'imagen': 'http://www.eltiempo.com/files/article_multimedia/uploads/2018/06/06/5b177c3b22c8e.jpeg',
	},
]
@login_required(redirect_field_name='login')
def publicacion(request):
	return render(request, 'publicaciones/publicaciones.html',{'publicaciones':noticias})