from django.contrib import admin
from django.urls import path
from instagram import views
from comentarios import views as comentarios_views
from publicaciones import views as publicaciones_views
from usuarios import views as usuarios_views
#from publicaciones import views
# from seguidores import views
# from usuarios import views
# from comentarios import views
# from likes import views

urlpatterns = [

		path('admin/', admin.site.urls),
		path('comentarios/', comentarios_views.comentario),
		path('publicaciones/', publicaciones_views.publicacion, name="publicaciones"),
		path('login/', usuarios_views.usuario, name="login"),
 #    path('likes/', views.like),
 		#path('publicaciones/', views.publicacion),
 #    path('seguidores/', views.seguidor),
 #    path('usuarios/', views.usuario),
     

]
