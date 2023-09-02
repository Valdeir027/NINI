from django import forms
from django.contrib import admin
from .models import Livro, Capitulo, Pagina

class PaginaInline(admin.TabularInline):
    model = Pagina
    extra = 1

class CapituloForm(forms.ModelForm):
    class Meta:
        model = Capitulo
        fields = '__all__'

class CapituloAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'livro')
    form = CapituloForm
    inlines = [PaginaInline]

class CapituloInline(admin.TabularInline):
    model = Capitulo
    inlines = [PaginaInline]
    extra = 1

class LivroAdmin(admin.ModelAdmin):
    list_display = ('titulo',)
    inlines = [CapituloInline]

admin.site.register(Livro, LivroAdmin)
admin.site.register(Capitulo, CapituloAdmin)
admin.site.register(Pagina)
 