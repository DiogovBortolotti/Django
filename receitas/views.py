from django.http import HttpResponse
from django.shortcuts import render
from utilitarios.fake_info import criar_receita

from .models import Receita


# Create your views here.
def home(request):
    receitas = Receita.objects.filter(
        publicacao=True).order_by('-id')
    return render(request, 'receitas/pages/home.html',
                  context={'receitas': receitas})  # [criar_receita() for _ in range(100)], })


def categoria(request, categoria_id):
    receitas = Receita.objects.filter(
        publicacao=True, categoria_id=categoria_id).order_by('-id')
    return render(request, 'receitas/pages/categoria.html',
                  context={'receitas': receitas})


def receita(request, id):
    return render(request, 'receitas/pages/receita.html',
                  context={'receita': criar_receita(),
                           'detail_page': True, })
