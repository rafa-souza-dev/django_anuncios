from django.urls import path

from anuncios import views

urlpatterns = [
    path('', views.home, name='home'),
    path('categoria/<int:categoria_id>/', views.categoria_filtrada, name='categoria'),
    path('anuncio/<int:anuncio_id>/', views.anuncio_filtrado, name='anuncio'),
    path('cadastrar/anuncio/', views.AnuncioCreate.as_view(), name='cadastrar-anuncio'),
    path('editar/anuncio/<int:pk>/', views.AnuncioUpdate.as_view(), name='editar-anuncio'),
    path('excluir/anuncio/<int:pk>/', views.AnuncioDelete.as_view(), name='excluir-anuncio'),
]
