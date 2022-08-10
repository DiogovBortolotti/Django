from django.http.response import Http404
from django.shortcuts import render

from .models import Receita


# Create your views here.
def home(request):
    receitas = Receita.objects.filter(
        publicacao=True,).order_by('-id')
    return render(request, 'receitas/pages/home.html',
                  context={'receitas': receitas})


def categoria(request, categoria_id):
    receitas = Receita.objects.filter(
        publicacao=True, categoria_id=categoria_id).order_by('-id')
    return render(request, 'receitas/pages/categoria.html',
                  context={'receitas': receitas,
                           'titulo': f'{receitas[0].categoria.nome} - Categoria'})


def receita(request, id):
    receita = Receita.objects.filter(
        publicacao=True, id=id).order_by('-id').first()

    return render(request, 'receitas/pages/receita.html',
                  context={'receita': receita,
                           'detail_page': True, })


def search(request):
    search_t = request.GET.get('q')
    if not search_t:
        raise Http404()
    return render(request, 'receitas/pages/search.html', {
        'page_title': f'Procurou por "{search_t}" |',
    })
