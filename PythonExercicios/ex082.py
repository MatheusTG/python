lista = []
par = lista[:]
impar = lista[:]
while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Você quer continuar? [S/N] ')).strip().upper()[0]
    if continuar in 'N':
        break
print('=-=' * 10, f'\nVocê digitou os valores {lista}')
print(f'Entre esses valores os pares são {par}')
print(f'Entre esses valores os ímpares são {impar}')
