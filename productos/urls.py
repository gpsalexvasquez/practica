from django.urls import path
from .views import *

urlpatterns = [
    path("productos/index", index_productos, name="index_productos")
]
