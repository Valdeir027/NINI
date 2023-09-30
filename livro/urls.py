from django.urls import path
from . import views

urlpatterns = [
    path('', views.LivroListView.as_view(), name='livros'),
    path('ler_livro/<int:livro_id>/', views.ler_livro, name='ler_livro'),
    path('ler_livro/<int:capitulo_id>/<int:pagina_numero>/', views.proxima_pagina, name='pagina_proxima'),
    path('criar_livro/', views.criar_livro, name='criar_livro'),
]
