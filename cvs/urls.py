from django.urls import path, include
from .views import *
urlpatterns = [
    path('match-resumes/', resume_matcher, name='resume_matcher'),
]