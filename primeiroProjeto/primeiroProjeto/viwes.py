from django.http import HttpResponse
from django.shortcuts import render


def hello(request):
    return render(request, 'index.html')


def article(request, year):
    return HttpResponse('O ano enviado foi: ' + str(year))


def lerdoBanco(nome):
    lista_nome = [
        {'nome': 'Pedro', 'idade': 25},
        {'nome': 'Estevam', 'idade': 22},
        {'nome': 'Joaquim', 'idade': 27},
        {'nome': 'Crhistian', 'idade': 19}
    ]


    for pessoa in lista_nome:
        if pessoa['nome'] == nome:
            print('If {}'.format(nome))
            return pessoa
    return {'nome': 'nao foi encontrado', 'idade': 0}
        


def fname(request, nome):
    result = lerdoBanco(nome)
    return HttpResponse('{} tem {} anos'.format(result['nome'], str(result['idade'])))


def fname2(request, nome):
    idade = lerdoBanco(nome)['idade']
    nome = lerdoBanco(nome)['nome']

    return render(request, 'pessoa.html', {'v_idade': idade, 'v_nome': nome})
