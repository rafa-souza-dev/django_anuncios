from django.contrib.auth import views as auth_views

from anuncios.models import Categoria


class Login(auth_views.LoginView):
    template_name = 'usuarios/login.html'
    extra_context = {'categorias': Categoria.objects.all()}


class Logout(auth_views.LogoutView):
    pass
