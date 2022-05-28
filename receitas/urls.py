from django.urls import path

from . import views

#from receitas.views import home


# http request (Cliente) < http response (Servidor)


urlpatterns = [
    path('', views.home),
    path('receita/<id>/', views.receita)
]
