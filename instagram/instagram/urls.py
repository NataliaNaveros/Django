from django.contrib import admin
from django.urls import path
from comentarios import views as cmt_views
from usuarios.views import *
from publicaciones.views import *
from likes.views import *
from seguidores.views import *
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [

		path('admin/', admin.site.urls),
		path('', login.as_view(), name='inicio'),
		path('registrarse', registrarse.as_view(), name='registrarse'),
		path('instagram', instagram.as_view(), name='instagram'), 
		path('perfil', perfil.as_view(), name='perfil'),
		path('cerrar_sesion', cerrar_sesion.as_view(), name='cerrar_sesion'), 
		path('perfil_subir', perfil_subir.as_view(), name='perfil_subir'), 
		path('perfil_editar', perfil_editar.as_view(), name='perfil_editar'), 
		path('seguir', seguir.as_view(), name='seguir'), 
		
		path('borrar_publicaciones', borrar_publicaciones.as_view(), name='borrar_publicaciones'), 
		path('me_gusta/<int:id>', me_gusta.as_view(), name='me_gusta'),

		path('comentarios', cmt_views.comentarios, name='comentarios'), 
		path('borrar_comentarios', cmt_views.borrar_comentarios, name='borrar_comentarios'),

]#+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
