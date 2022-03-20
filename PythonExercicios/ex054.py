from datetime import date
ano = date.today().year
cont1 = 0
cont2 = 0
for nasc in range(1, 8):
    n = int(input('{}° data de nascimento: '.format(nasc)))
    idade = ano - n
    if idade >= 21:
        cont1 += 1
    else:
        cont2 += 1
print('Há {} pessoas maiores de idade nessa lista e {} menores!'.format(cont1, cont2))
