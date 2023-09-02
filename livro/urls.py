from django.urls import path
from . import views

urlpatterns = [
    path('criar_livro/', views.criar_livro, name='criar_livro'),
    path('editar_livro/<int:livro_id>/', views.editar_livro, name='editar_livro'),
]
