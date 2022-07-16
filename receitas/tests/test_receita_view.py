
# from django.contrib.auth.models import User

from http.client import responses

from django.test import TestCase
from django.urls import resolve, reverse
from receitas import views
from receitas.models import Categoria, Receita, User

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


    def test_receitas_home_template_loads_receitas(self):
        categoria = Categoria.objects.create(nome='Categoria')
        # categoria = Categoria(nome='Categoria')
        # categoria.full_clean()
        # categoria.save()
        autor = User.objects.create_user(first_name='user',
                                         last_name='name',
                                         username='username',
                                         password='123456',
                                         email='username@example.com')

        receita = Receita.objects.create(
            categoria=categoria,
            usuario=autor,
            titulo='Receita Titulo',
            descricao='Receita Descrição',
            slug='receita-slug',
            tempo_preparo=10,
            tipo_tempo='Minutos',
            quantidade_porcao=5,
            tipo_unitario='Porções',
            etapa_de_preparo='Etapa de Preparação',
            etapa_de_preparo_e_html=False,
            capa='colocar_algo_se_nao_da_erro_pois_nao_possui_imagem',
            publicacao=True,
        )
        resposta = self.client.get(reverse('receitas:home'))
        resposta_receitas = resposta.context['receitas']
        self.assertEqual(resposta_receitas.first().titulo, 'Receita Titulo')

        content = resposta.content.decode('utf-8')
        self.assertIn('Receita Titulo', content)
        self.assertIn('10 Minutos', content)
        # categoria = Categoria(nome='Categoria')
        # categoria.full_clean()
        # categoria.save()

        pass
