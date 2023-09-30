from django.shortcuts import render, redirect
from .models import Livro, Capitulo, Pagina
from .forms import LivroForm, CapituloForm, PaginaForm
from django.views import generic


def criar_livro(request):
    if request.method == 'POST':
        livro_form = LivroForm(request.POST)
        if livro_form.is_valid():
            novo_livro = livro_form.save()
            return redirect('editar_livro', livro_id=novo_livro.id)
    else:
        livro_form = LivroForm()
    return render(request, 'livro/criar_livro.html', {'livro_form': livro_form})


def editar_livro(request, livro_id):
    livro = Livro.objects.get(id=livro_id)
    capitulos = Capitulo.objects.filter(livro=livro)

    if request.method == 'POST':
        capitulo_form = CapituloForm(request.POST)
        if capitulo_form.is_valid():
            novo_capitulo = capitulo_form.save(commit=False)
            novo_capitulo.livro = livro
            novo_capitulo.save()
            return redirect('editar_livro', livro_id=livro_id)
    else:
        capitulo_form = CapituloForm()

    if request.method == 'POST':
        pagina_form = PaginaForm(request.POST)
        if pagina_form.is_valid():
            nova_pagina = pagina_form.save(commit=False)

            # Obter o último capítulo para associar a página
            ultimo_capitulo = capitulos.order_by('-id').first()
            if ultimo_capitulo:
                nova_pagina.capitulo = ultimo_capitulo
                nova_pagina.numero = Pagina.objects.filter(capitulo=ultimo_capitulo).count() + 1
            else:
                # Se não houver capítulos, crie um novo
                novo_capitulo = Capitulo(livro=livro, titulo='Capítulo Inicial')
                novo_capitulo.save()
                nova_pagina.capitulo = novo_capitulo
                nova_pagina.numero = 1

            nova_pagina.save()
            return redirect('editar_livro', livro_id=livro_id)
    else:
        pagina_form = PaginaForm()

    return render(request, 'livro/editar_livro.html', {'livro': livro, 'capitulos': capitulos, 'capitulo_form': capitulo_form, 'pagina_form': pagina_form})


class LivroListView(generic.ListView):
    model = Livro
    context_object_name = 'list_livros'
    queryset = Livro.objects.all()
    template_name = 'livro/listar_livros.html'



    def get_queryset(self):
        return Livro.objects.all()
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(LivroListView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        return context