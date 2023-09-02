from django import forms
from .models import Livro, Capitulo, Pagina

class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = ['titulo']

class CapituloForm(forms.ModelForm):
    class Meta:
        model = Capitulo
        fields = ['titulo']

class PaginaForm(forms.ModelForm):
    class Meta:
        model = Pagina

        fields = ['conteudo']