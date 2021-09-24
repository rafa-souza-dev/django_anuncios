from django.urls import path

from anuncios import views

urlpatterns = [
    path('', views.home, name='home'),
    path('bem-vindo/', views.Home.as_view(), name='home2'),
    path('resultado/', views.resultado, name='resultado'),
    path('categoria/<int:categoria_id>/', views.categoria_filtrada, name='categoria'),
    path('anuncio/<int:anuncio_id>/', views.anuncio_filtrado, name='anuncio'),
    path('cadastrar/anuncio/', views.AnuncioCreate.as_view(), name='cadastrar-anuncio'),
    path('cadastrar/categoria/', views.CategoriaCreate.as_view(), name='cadastrar-categoria'),
    path('editar/anuncio/<int:pk>/', views.AnuncioUpdate.as_view(), name='editar-anuncio'),
    path('excluir/anuncio/<int:pk>/', views.AnuncioDelete.as_view(), name='excluir-anuncio'),
    path('tabela-anuncios/', views.AnuncioList.as_view(), name='tabela-anuncios'),
]
