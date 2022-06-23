# from inspect import signature
from random import randint

from faker import Faker


def rand_ratio():
    return randint(840, 900), randint(473, 573)


fake = Faker('pt_BR')
# print(signature(fake.random_number))


def criar_receita():
    return {
        'id': fake.random_number(digits=2, fix_len=True),
        'titulo': fake.sentence(nb_words=6),
        'descricao': fake.sentence(nb_words=12),
        'tempo_preparo': fake.random_number(digits=2, fix_len=True),
        'tipo_tempo': 'Minutos',
        'quantidade_porcao': fake.random_number(digits=2, fix_len=True),
        'tipo_unitario': 'Porção',
        'etapa_de_preparo': fake.text(3000),
        'data_criacao': fake.date_time(),
        'autor': {
            'primeiro_nome': fake.first_name(),
            'segundo_nome': fake.last_name(),
        },
        'categoria': {
            'nome': fake.word()
        },
        'capa': {
            'url': 'https://loremflickr.com/%s/%s/food,cook' % rand_ratio(),
        }
    }


if __name__ == '__main__':
    from pprint import pprint
    pprint(criar_receita())
