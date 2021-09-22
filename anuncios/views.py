from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.urls import reverse_lazy

from anuncios import models


def home(request):
    categorias = models.Categoria.objects.all()
    ultimos_anuncios = models.Anuncio.objects.all()[:12]

    return render(request, 'home.html', {
        'categorias': categorias,
        'ultimos_anuncios': ultimos_anuncios
    })


def categoria_filtrada(request, categoria_id):
    categoria = get_object_or_404(models.Categoria, id=categoria_id)

    categorias = models.Categoria.objects.all()

    anuncios = models.Anuncio.objects.filter(categoria=categoria)

    return render(request, 'home.html', {
        'categorias': categorias,
        'ultimos_anuncios': anuncios,
        'categoria': categoria,
    })


def anuncio_filtrado(request, anuncio_id):
    anuncio = get_object_or_404(models.Anuncio, id=anuncio_id)

    categorias = models.Categoria.objects.all()

    return render(request, 'anuncio.html', {
        'categorias': categorias,
        'anuncio': anuncio,
    })


class AnuncioCreate(generic.CreateView):
    model = models.Anuncio
    fields = ['titulo', 'descricao', 'preco', 'categoria']
    template_name = 'form.html'
    success_url = reverse_lazy('home')
    extra_context = {'categorias': models.Categoria.objects.all()}


class AnuncioUpdate(generic.UpdateView):
    model = models.Anuncio
    fields = ['titulo', 'descricao', 'preco', 'categoria']
    template_name = 'form.html'
    success_url = reverse_lazy('home')
    extra_context = {'categorias': models.Categoria.objects.all()}

