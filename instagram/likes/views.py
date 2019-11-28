from django.shortcuts import render, redirect
from usuarios.models import *
from publicaciones.models import *
from comentarios.models import *
from seguidores.models import *
from likes.models import *
from django.views.generic import TemplateView
from datetime import datetime, timedelta, time

class me_gusta(TemplateView):
    template_name = 'usuarios/perfil.html'
    def get(self, request, *args, **kwargs):
        id_publicacion = publicaciones.objects.get(pk = self.kwargs['id'])
        id_usuario = usuarios.objects.get(pk = request.session['usuario_id'])
        existe = likes.objects.filter(publicacion=id_publicacion, usuario=id_usuario).count()
        if existe == 0:
            crear = likes.objects.create(publicacion=id_publicacion, usuario=id_usuario)
        else:
            borrar = likes.objects.filter(publicacion=id_publicacion, usuario=id_usuario)
            borrar.delete()
        return redirect('instagram')
