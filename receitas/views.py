from django.shortcuts import render

from .models import Receita


# Create your views here.
def home(request):
    receitas = Receita.objects.filter(
        publicacao=True,).order_by('-id')
    return render(request, 'receitas/pages/home.html',
                  context={'receitas': receitas})
    # receitas = Receita.objects.filter(
    #   publicacao=True).order_by('-id')
   # return render(request, 'receitas/pages/home.html',
    #            context={'receitas': receitas})  # [criar_receita() for _ in range(100)], })


def categoria(request, categoria_id):
    receitas = Receita.objects.filter(
        publicacao=True, categoria_id=categoria_id).order_by('-id')
    return render(request, 'receitas/pages/categoria.html',
                  context={'receitas': receitas,
                           'titulo': f'{receitas[0].categoria.nome} - Categoria'})
    # receitas = Receita.objects.filter(
    #  publicacao=True, categoria_id=categoria_id).order_by('-id')

    # if not receitas:
    #   raise Http404('Não Deveria Ocorrer')
    # return HttpResponse(content='Opa Voce não deveria estár aqui', status=404)


def receita(request, id):
    receita = Receita.objects.filter(
        publicacao=True, id=id).order_by('-id').first()

    return render(request, 'receitas/pages/receita.html',
                  context={'receita': receita,
                           'detail_page': True, })
