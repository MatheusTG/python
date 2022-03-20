def sorteia(*tupla):
    from random import randint
    from time import sleep
    print('Sorteando 5 valores ', end='')
    for c in range(5):
        sorteio = randint(1, 9)
        print(sorteio, end=' ')
        sleep(0.5)
        lista.append(sorteio)
    print('Pronto!', end='')


def somapar():
    soma = 0
    for d in lista:
        if d % 2 == 0:
            soma += d
    print(f'Se somarmos os valores pares de {lista} teremos o valor {soma}!')


lista = list()
sorteia(), print(), somapar()
