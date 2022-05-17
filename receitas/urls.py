from django.urls import path

from receitas.views import inicio

# http request (Cliente) < http response (Servidor)


urlpatterns = [
    path('', inicio)
]
