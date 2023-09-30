from django import forms
from .models import Livro, Capitulo, Pagina

class PaginaForm(forms.ModelForm):
    class Meta:
        model = Pagina
        fields = ['conteudo']
        
class CapituloForm(forms.ModelForm):
    class Meta:
        model = Capitulo
        fields = ['titulo']  

class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = ['titulo']     

PaginaFormSet = forms.inlineformset_factory(Capitulo, Pagina, form=PaginaForm, extra=1, can_delete=False)
CapituloFormSet = forms.inlineformset_factory(Livro, Capitulo, form=CapituloForm, extra=1, can_delete=False)





