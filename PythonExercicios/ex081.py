lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Você quer continuar? [S/N] ')).strip().upper()[0]
    if continuar in 'N':
        break
print('=-=' * 15)
lista.sort(reverse=True)
print(f'Foram digitados {len(lista)} valores!')
print(f'Lista em ordem decrecente: {lista}')
lista.sort()
if 5 in lista:
    print(f'O valor 5 foi digitado e está na posição {lista.index(5)}!')
else:
    print('O valor 5 não foi encontrado na lista!')
