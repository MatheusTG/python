from ex115.lib.interface import *


def arquivoexiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criararquivo(nome):
    try:
        a = open(nome, 'wt+')
    except:
        print('Erro ao ler arquivo!')


def lerarquivo(nome):
    try:
        a = open(nome, 'rt')
        titulo('PESSOAS CADASTRADAS')
    except:
        print('Erro, ao ler arquivo!')
    else:
        print(a.readlines())
