lista = []
menor = maior = 0
for c in range(0, 5):
    lista.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
        menor = maior = lista[c]
    if lista[c] < menor:
        menor = lista[c]
    if lista[c] > maior:
        maior = lista[c]
print('=-=' * 14)
print(f'Os valores digitados foram {lista}')
print(f'O menor valor digitado foi {menor} nas posições ', end='')
for p, v in enumerate(lista):
    if v == menor:
        print(f'{p}... ', end='')
print()
print(f'O maior valor digitado foi {maior} nas posições ', end='')
for p, v in enumerate(lista):
    if v == maior:
        print(f'{p}... ', end='')
print()