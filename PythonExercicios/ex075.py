tupla = (int(input('Digite um número: ')),
         int(input('Digite outro número: ')),
         int(input('Digite mais um número: ')),
         int(input('Digite o ultimo número: ')))
print(f'Você digitou os valores {tupla}')
print(f'O valor 9 aprareceu {tupla.count(9)} vezes!')
if 3 in tupla:
    print(f'O valor 3 apareceu na {tupla.index(3) + 1}° posição!')
else:
    print('O três não apareceu em nenhum aposição!')
print(f'Os valores pares digitados são: ', end='')
for c in sorted(tupla):
    if c % 2 == 0:
        print(f'{c}', end=' ')
