from django.test import TestCase

from anuncios import models


class TestModelCategoria(TestCase):
    def setUp(self) -> None:
        self.categoria = models.Categoria(titulo='julietes')

    def test_str_de_categoria_deve_retornar_seu_titulo(self):
        esperado = 'julietes'
        resultado = str(self.categoria)
        self.assertEqual(esperado, resultado)


class TestModelAnuncio(TestCase):
    def setUp(self) -> None:
        self.categoria = models.Categoria(titulo='imóveis')
        self.anuncio = models.Anuncio(
            titulo='Sofá',
            preco=2000,
            categoria=self.categoria,
        )

    def test_str_anuncio_deve_retornar_titulo_e_preco(self):
        esperado = 'Sofá 2000'
        resultado = str(self.anuncio)
        self.assertEqual(esperado, resultado)
