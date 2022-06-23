from django.urls import path

from . import views

app_name = 'receitas'

#from receitas.views import home


# http request (Cliente) < http response (Servidor)


urlpatterns = [
    path('', views.home, name="home"),

    path('receita/categoria/<int:categoria_id>/',
         views.categoria, name="categoria"),

    path('receita/<int:id>/', views.receita, name="receita")

]
