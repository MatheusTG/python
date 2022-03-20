soma = 0
contador = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        contador += 1
        soma += c
print('Existem {} númeos que são inpares e multiplos de 3, '.format(contador), end='')
print('e a soma deles é igual a {}!'.format(soma))
