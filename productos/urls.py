from django.urls import path
from .views import *

urlpatterns = [
    path("productos/index", index_productos, name="index_productos"),
    path("productos/nuevo", registrar_producto, name="nuevo_producto"),
    path("productos/eliminar/<int:id>", eliminar_producto, name="eliminar_producto"),
    path("productos/editar/<int:producto_id>", editar_producto, name="editar_producto"),
    path('chatbot/', chatbot_view, name='chatbot'),
]
