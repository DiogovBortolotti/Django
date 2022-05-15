from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def inicio(request):
    return render(request, 'receitas/inicio.html',
                  context={'name': 'Diogo', })


def contato(request):
    return render(request, 'temp.html')


def sobre(request):
    return render(request, 'receitas/sobre.html')
