
# from django.contrib.auth.models import User  from django.test import TestCase

from django.urls import resolve, reverse
from receitas import views

from .teste_receita_base import ReceitaTesteBase

# Create your tests here.
# pip install pytest-watch
# ptw


class ReceitasViewsTest(ReceitaTesteBase):

    def test_receitas_views_functions(self):
        view_home = resolve(reverse('receitas:home'))
        self.assertIs(view_home.func, views.home)

    def test_categoria_views_functions(self):
        view_categoria = resolve(reverse('receitas:categoria',
                                         kwargs={'categoria_id': 1}))
        self.assertIs(view_categoria.func, views.categoria)

    def test_receitas_home_view_return_status(self):
        resposta = self.client.get(reverse('receitas:home'))
        self.assertEqual(resposta.status_code, 200)

    def test_detalhes_views_functions(self):
        view_receita = resolve(reverse('receitas:receita',
                                       kwargs={'id': 1}))
        self.assertIs(view_receita.func, views.receita)

    def test_receitas_home_view_loads_template(self):
        resposta = self.client.get(reverse('receitas:home'))
        self.assertTemplateUsed(resposta, 'receitas/pages/home.html')

    def test_receitas_home_template_receitas_not_found(self):
        resposta = self.client.get(reverse('receitas:home'))
        self.assertIn('<h1>Não há Receitas, tente novamente mais tarde! </h1>',
                      resposta.content.decode('utf-8')
                      )


# com conteudo testes:
