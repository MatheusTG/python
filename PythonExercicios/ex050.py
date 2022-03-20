s = 0
cont = 0
for c in range(1, 7):
        num = int(input('{}° Valor: '.format(c)))
        if c % 2 == 0:
                s += c
                cont += 1
print('Você digitou {} números PARES e a soma deles é {}!'.format(cont, s))
