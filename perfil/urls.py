from django.urls import path, include
from .views import *
urlpatterns = [
    path('perfil/index', lista_perfiles, name='lista_perfiles'),
    path('crear/', crear_perfil, name='crear_perfil'),
    path('editar/<int:pk>/', editar_perfil, name='editar_perfil'),
    path('eliminar/<int:pk>/', eliminar_perfil, name='eliminar_perfil'),
    
]