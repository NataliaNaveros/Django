from django.contrib import admin
from django.urls import path

from publicaciones import views
from seguidores import views
from usuarios import views
from comentarios import views
from likes import views

urlpatterns = [

	path('comentarios/', views.comentarios),
    path('likes/', views.likes),
    path('publicaciones/', views.publicaciones),
    path('seguidores/', views.seguidores),
    path('usuarios/', views.usuarios),
    

]
