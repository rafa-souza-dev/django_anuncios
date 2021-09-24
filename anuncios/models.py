from django.db import models
from django.contrib.auth.models import User


class Categoria(models.Model):
    titulo = models.CharField(max_length=40)

    def __str__(self):
        return self.titulo


class Anuncio(models.Model):
    titulo = models.CharField(max_length=40)
    descricao = models.TextField(null=True, blank=True)
    preco = models.DecimalField(max_digits=11, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    criado_em = models.DateTimeField(auto_now_add=True)
    editado_em = models.DateTimeField(auto_now=True)

    usuario = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.titulo
