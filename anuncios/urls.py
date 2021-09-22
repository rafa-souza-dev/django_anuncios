from django.urls import path

from .views import home, categoria_filtrada, anuncio_filtrado, AnuncioCreate, AnuncioUpdate

urlpatterns = [
    path('', home, name='home'),
    path('categoria/<int:categoria_id>', categoria_filtrada, name='categoria'),
    path('anuncio/<int:anuncio_id>', anuncio_filtrado, name='anuncio'),
    path('cadastrar/anuncio/', AnuncioCreate.as_view(), name='cadastrar-anuncio'),
    #path('editar/anuncio/<int:pk>', AnuncioUpdate.as_view(), name='editar-anuncio'),
]
