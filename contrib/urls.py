from django.urls import path
from . import views

urlpatterns = [
    path('perfil_autor/', views.perfil_autor, name='perfil_autor'),
]