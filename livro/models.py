from django.db import models
from contrib.models import Autor



class Livro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return f"{self.titulo} - Autor: {self.autor.user.username}"

class Capitulo(models.Model):
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE, default = False)
    titulo = models.CharField(max_length=100, default = False)
    def __str__(self):
        return self.titulo

class Pagina(models.Model):
    capitulo = models.ForeignKey(Capitulo, on_delete=models.CASCADE, default = False)
    numero = models.PositiveIntegerField(null=True, blank=True, default = False)
    conteudo = models.TextField(default = False)
