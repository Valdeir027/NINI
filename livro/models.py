from django.db import models

class Livro(models.Model):
    titulo = models.CharField(max_length=100)

    def __str__(self):
        return self.titulo

class Capitulo(models.Model):
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    def __str__(self):
        return self.titulo

class Pagina(models.Model):
    capitulo = models.ForeignKey(Capitulo, on_delete=models.CASCADE)
    numero = models.PositiveIntegerField(null=True, blank=True)
    conteudo = models.TextField()
