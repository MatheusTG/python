matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = maior = cont = 0
for l in range(3):
    for c in range(3):
        matriz[l][c] = (int(input(f'Digite uma valor para [{l}, {c}]: ')))
print('=-=' * 15)
for l in range(3):
    for c in range(3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]
    print()
print('=-=' * 15)
print(f'A soma dos valores pares é {spar}!')
soma = matriz[0][2] + matriz[1][2] + matriz[2][2]
print(f'A soma dos valores da terceira coluna é {soma}! ')
for r in matriz[1]:
    cont += 1
    if cont == 1 or r > maior:
        maior = r
print(f'O maior valor da segunda linha é {maior}!')
