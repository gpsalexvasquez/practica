from django.urls import path
from .views import *

urlpatterns = [
    path('home/', public_home, name='home'),
    path('home/admin', home_admin, name='home_admin'),
    path('login/', login, name='login'),
    path('salir/', salir, name='salir'),
]