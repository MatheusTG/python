from random import randint
tupla = randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10)
print('Os valores sorteados são: ', end='')
cont = menor = maior = 0
for c in tupla:
    print(c, end=' ')
print(f'\nO menor valor sorteado foi {min(tupla)}')
print(f'O maior valor sorteado foi {max(tupla)}')
