from django.contrib import admin

from .models import Categoria, Receita

# admin serve para fazer crud da area administrativa


class CategoriaAdmin(admin.ModelAdmin):
    ...


@admin.register(Receita)  # registrar pode usar o decorate
class ReceitaAdmin(admin.ModelAdmin):
    ...


admin.site.register(Categoria, CategoriaAdmin)
