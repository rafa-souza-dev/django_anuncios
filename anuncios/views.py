from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from braces.views import GroupRequiredMixin

from anuncios import models


def home(request):
    categorias = models.Categoria.objects.all()
    ultimos_anuncios = models.Anuncio.objects.all()[:12]

    return render(request, 'anuncios/home.html', {
        'categorias': categorias,
        'ultimos_anuncios': ultimos_anuncios
    })


def categoria_filtrada(request, categoria_id):
    categoria = get_object_or_404(models.Categoria, id=categoria_id)

    categorias = models.Categoria.objects.all()

    anuncios = models.Anuncio.objects.filter(categoria=categoria)

    return render(request, 'anuncios/home.html', {
        'categorias': categorias,
        'ultimos_anuncios': anuncios,
        'categoria': categoria,
    })


def anuncio_filtrado(request, anuncio_id):
    anuncio = get_object_or_404(models.Anuncio, id=anuncio_id)

    categorias = models.Categoria.objects.all()

    return render(request, 'anuncios/anuncio.html', {
        'categorias': categorias,
        'anuncio': anuncio,
    })


def resultado(request):
    valor_digitado = request.GET.get('resultado', 'This is a default value')
    anuncios_filtrados = models.Anuncio.objects.filter(titulo__icontains=valor_digitado)
    context = {
        'valor_digitado': valor_digitado,
        'anuncios_filtrados': anuncios_filtrados
    }
    return render(request, 'home.html', context)


class Home(generic.TemplateView):
    template_name = "anuncios/home2.html"
    extra_context = {'categorias': models.Categoria.objects.all()}


class CategoriaCreate(GroupRequiredMixin, LoginRequiredMixin, generic.CreateView):
    model = models.Categoria
    extra_context = {'categorias': models.Categoria.objects.all()}
    template_name = 'anuncios/form.html'
    fields = ['titulo']
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('login')
    group_required = u"Administrador"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Cadastrar Categoria"
        context['texto'] = "Cadastrar"
        context['cor'] = "primary"

        return context


class AnuncioCreate(GroupRequiredMixin, LoginRequiredMixin, generic.CreateView):
    model = models.Anuncio
    fields = ['titulo', 'descricao', 'preco', 'categoria']
    template_name = 'anuncios/form.html'
    success_url = reverse_lazy('home')
    extra_context = {'categorias': models.Categoria.objects.all()}
    login_url = reverse_lazy('login')
    group_required = [u"Administrador", u"Anunciador"]

    def form_valid(self, form):
        form.instance.usuario = self.request.user

        url = super().form_valid(form)

        return url

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Cadastrar Anúncio"
        context['texto'] = "Cadastrar"
        context['cor'] = "primary"

        return context


class AnuncioUpdate(GroupRequiredMixin, LoginRequiredMixin, generic.UpdateView):
    model = models.Anuncio
    fields = ['titulo', 'descricao', 'preco', 'categoria']
    template_name = 'anuncios/form.html'
    success_url = reverse_lazy('home')
    extra_context = {'categorias': models.Categoria.objects.all()}
    login_url = reverse_lazy('login')
    group_required = u"Administrador"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Editar Anúncio"
        context['texto'] = "Editar"
        context['cor'] = "yellow"

        return context


class AnuncioDelete(GroupRequiredMixin, LoginRequiredMixin, generic.DeleteView):
    model = models.Anuncio
    template_name = 'anuncios/form.html'
    success_url = reverse_lazy('home')
    extra_context = {'categorias': models.Categoria.objects.all()}
    login_url = reverse_lazy('login')
    group_required = u"Administrador"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Excluir Anúncio"
        context['subtitulo'] = f"Tem certeza que quer excluir o anúncio?"
        context['texto'] = "Excluir"
        context['cor'] = "negative"

        return context


class AnuncioList(generic.ListView):
    template_name = 'anuncios/tabela.html'
    model = models.Anuncio
    extra_context = {'categorias': models.Categoria.objects.all()}
