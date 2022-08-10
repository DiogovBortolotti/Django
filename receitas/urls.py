from django.urls import path

from . import views

app_name = 'receitas'

# http request (Cliente) > < http response (Servidor)


urlpatterns = [
    path('', views.home, name="home"),

    path('receita/categoria/<int:categoria_id>/',
         views.categoria, name="categoria"),
    path('receita/<int:id>/', views.receita, name="receita"),
    path('receita/search/', views.search, name="search"),


]
