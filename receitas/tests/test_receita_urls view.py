
from django.test import TestCase
from django.urls import resolve, reverse
from receitas import views

# Create your tests here.
# pip install pytest-watch
# ptw


class ReceitasViewsTest(TestCase):
    def test_receitas_views_functions(self):
        view_home = resolve(reverse('receitas:home'))
        self.assertIs(view_home.func, views.home)

    def test_categoria_views_functions(self):
        view_categoria = resolve(reverse('receitas:categoria',
                                         kwargs={'categoria_id': 1}))
        self.assertIs(view_categoria.func, views.categoria)

    def test_detalhes_views_functions(self):
        view_receita = resolve(reverse('receitas:receita', kwargs={'id': 1}))
        self.assertIs(view_receita.func, views.receita)


''


''
