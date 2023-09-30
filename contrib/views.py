from django.shortcuts import render, redirect
from .models import Autor
from .forms import AutorForm

def perfil_autor(request):
    # Verifique se o usuário já possui um perfil de autor
    try:
        autor = request.user.atutor
    except Autor.DoesNotExist:
        autor = None

    if request.method == 'POST':
        if autor:
            # Se o autor já existe, atualize os dados do perfil
            autor_form = AutorForm(request.POST, instance=autor)
        else:
            # Se não existe, crie um novo perfil de autor
            autor_form = AutorForm(request.POST)

        if autor_form.is_valid():
            novo_autor = autor_form.save(commit=False)
            novo_autor.user = request.user  # Associe o perfil de autor ao usuário atual
            novo_autor.save()
            return redirect('perfil_autor')
    else:
        if autor:
            # Se o autor já possui um perfil, preencha o formulário com seus dados
            autor_form = AutorForm(instance=autor)
        else:
            # Se não possui um perfil, crie um novo formulário em branco
            autor_form = AutorForm()

    return render(request, 'contrib/perfil_autor.html', {'autor_form': autor_form})
