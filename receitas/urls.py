from django.urls import path

from receitas.views import contato, inicio, sobre

# http request (Cliente) < http response (Servidor)


urlpatterns = [
    path('', inicio),
    path('sobre/', sobre),
    path('contato/', contato)
]
