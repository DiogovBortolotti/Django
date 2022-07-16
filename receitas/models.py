from email.policy import default
from pickle import TRUE

from django.contrib.auth.models import User
from django.db import models


class Categoria(models.Model):
    nome = models.CharField(max_length=250)
# defini o modelo para retornar o modelo como string

    def __str__(self):
        return self.nome


class Receita(models.Model):
    titulo = models.CharField(max_length=80)
    descricao = models.CharField(max_length=200)
    slug = models.SlugField()
    tempo_preparo = models.IntegerField()
    tipo_tempo = models.TextField(max_length=30)
    quantidade_porcao = models.IntegerField()
    tipo_unitario = models.TextField(max_length=30)
    etapa_de_preparo = models.TextField(max_length=1000)
    etapa_de_preparo_e_html = models.BooleanField(default=False)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    publicacao = models.BooleanField(default=False)
    capa = models.ImageField(
        upload_to='receitas/capa/%Y/%m/%d/', blank=True, null=True)
    categoria = models.ForeignKey(
        Categoria, on_delete=models.SET_NULL, null=True, blank=True,
        default=None,
    )
    usuario = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True
    )

    def __str__(self):
        return self.titulo
# Create your models here.
