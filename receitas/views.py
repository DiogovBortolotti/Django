from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'receitas/pages/home.html',
                  context={'name': 'Diogo', })


def receita(request, id):
    return render(request, 'receitas/pages/receita.html',
                  context={'name': 'Diogo', })
