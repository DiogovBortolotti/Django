
from django.test import TestCase
from django.urls import resolve, reverse

# Create your tests here.
# pip install pytest-watch
# ptw
# manage.py -v0 até 3


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
