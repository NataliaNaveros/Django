from django.shortcuts import render, redirect
from usuarios.models import *
from publicaciones.models import *
from comentarios.models import *
from seguidores.models import *
from likes.models import *
from django.views.generic import TemplateView
from datetime import datetime, timedelta, time

class comentarios(TemplateView):
    template_name = 'publicaciones/publicaciones.html'
    def post(self, request, *args, **kwargs):
        id_publicacion = publicaciones.objects.get(pk = request.POST['publicacion'])
        id_usuario = usuarios.objects.get(pk = request.session['usuario_id'])
        if request.POST['comentario'] != '':
            crear = comentarios.objects.create(publicacion=id_publicacion, usuario=id_usuario, mensaje=request.POST['comentario'])
            return redirect('instagram')

class borrar_comentarios(TemplateView):
    template_name = 'publicaciones/publicaciones.html'
    def post(self, request, *args, **kwargs):
        borrar = comentarios.objects.filter(id=request.POST['comentario_id'])
        borrar.delete()
        return redirect('instagram')