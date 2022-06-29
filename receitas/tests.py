from turtle import home

from django.test import TestCase
from django.urls import resolve, reverse

from receitas import views

# Create your tests here.
# pip install pytest-watch
# ptw


class ReceitasUrlsTest(TestCase):
    def test_pytest_ok(self):
        print('hello')
        1 == 1, 'Deu erro pq não e igual'

    def test_receitas_home_url(self):
        home_url = reverse('receitas:home')
        self.assertEqual(home_url, '/')

    def test_receitas_categoria_url(self):
        url_categoria = reverse('receitas:categoria',
                                kwargs={'categoria_id': 1})
        self.assertEqual(url_categoria, '/receita/categoria/1/')

    def test_receitas_receita_url(self):
        url_receita = reverse('receitas:receita', kwargs={'id': 1})
        self.assertEqual(url_receita, '/receita/1/')


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
