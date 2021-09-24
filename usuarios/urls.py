from django.urls import path

from usuarios import views

urlpatterns = [
    path('login/', views.Login.as_view(), name="login"),
    path('logout', views.Logout.as_view(), name="logout"),

    path('registrar', views.UsuarioCreate.as_view(), name="registrar"),
    path('atualizar-dados/', views.PerfilUpdate.as_view(), name="atualizar-dados"),
]
