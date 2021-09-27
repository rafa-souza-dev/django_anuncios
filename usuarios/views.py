from django.contrib.auth import views as auth_views
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.models import User, Group
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from anuncios.models import Categoria
from .forms import UsuarioForm
from .models import Perfil


class Login(auth_views.LoginView):
    template_name = 'usuarios/login.html'
    extra_context = {'categorias': Categoria.objects.all()}
    success_url = reverse_lazy('home2')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Fazer Login"
        context['texto'] = "Entrar"

        return context


class Logout(auth_views.LogoutView):
    pass


class UsuarioCreate(CreateView):
    template_name = 'usuarios/login.html'
    form_class = UsuarioForm
    extra_context = {'categorias': Categoria.objects.all()}
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        grupo = get_object_or_404(Group, name="Anunciador")

        url = super().form_valid(form)

        self.object.groups.add(grupo)
        self.object.save()

        Perfil.objects.create(usuario=self.object)

        return url

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Criar Conta"
        context['texto'] = "Confirmar"
        context['fluid'] = "fluid"

        return context


class PerfilUpdate(LoginRequiredMixin, UpdateView):
    template_name = "anuncios/form.html"
    model = Perfil
    fields = ['nome_completo', 'cpf', 'telefone']
    success_url = reverse_lazy('home2')
    extra_context = {'categorias': Categoria.objects.all()}
    login_url = reverse_lazy('login')

    def get_object(self, queryset=None):
        self.object = get_object_or_404(Perfil, usuario=self.request.user)

        return self.object

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Meu Perfil"
        context['texto'] = "Salvar"
        context['cor'] = "yellow"

        return context
