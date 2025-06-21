from django.urls import path
from .views import *

urlpatterns = [
    path('transcriber/index', index, name="transcriber_index")
]

