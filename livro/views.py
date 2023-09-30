from django.shortcuts import render, redirect, get_object_or_404
from .models import Livro, Capitulo, Pagina
from django.views import generic


from .forms import LivroForm, CapituloFormSet, PaginaFormSet

def criar_livro(request):
    if request.method == 'POST':
        livro_form = LivroForm(request.POST)
        capitulo_formset = CapituloFormSet(request.POST, prefix='capitulo')
        pagina_formset = PaginaFormSet(request.POST, prefix='pagina')

        if livro_form.is_valid() and capitulo_formset.is_valid() and pagina_formset.is_valid():
            livro = livro_form.save(commit=False)
            livro.autor = request.user.atutor
            livro.save()

            capitulo_instances = capitulo_formset.save(commit=False)
            for capitulo in capitulo_instances:
                capitulo.livro = livro
                capitulo.save()

            pagina_instances = pagina_formset.save(commit=False)
            for capitulo, paginas in zip(capitulo_instances, pagina_instances):
                paginas.capitulo = capitulo
                paginas.save()

            return redirect('ler_livro', livro_id=livro.id)

    else:
        livro_form = LivroForm()
        capitulo_formset = CapituloFormSet(prefix='capitulo')
        pagina_formset = PaginaFormSet(prefix='pagina')

    return render(
        request,
        'livro/criar_livro.html',
        {'livro_form': livro_form, 'capitulo_formset': capitulo_formset, 'pagina_formset': pagina_formset}
    )


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
        context['list_livros'] = Livro.objects.select_related('autor').all()
        return context
    


def ler_livro(request, livro_id):
    livro = get_object_or_404(Livro, id=livro_id)
    capitulos = Capitulo.objects.filter(livro=livro)
    return render(request, 'livro/ler_livro.html', {'livro': livro, 'capitulos': capitulos})



def proxima_pagina(request, capitulo_id, pagina_numero):
    capitulo = get_object_or_404(Capitulo, id=capitulo_id)
    proxima_pagina_numero = int(pagina_numero) + 1

    if proxima_pagina_numero <= capitulo.pagina_set.count():
        return render(request, 'livro/pagina.html', {'pagina': capitulo.pagina_set.get(numero=proxima_pagina_numero)})

    proximo_capitulo_numero = capitulo.numero + 1
    proximo_capitulo = Capitulo.objects.filter(livro=capitulo.livro, numero=proximo_capitulo_numero).first()
    
    if proximo_capitulo:
        return render(request, 'livro/capitulo.html', {'capitulo': proximo_capitulo})
    else:
        # Não há próximo capítulo, redirecione para onde for necessário
        return render(request, 'livro/fim.html')