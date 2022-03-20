'''from math import sqrt
n1 = float(input('Cateto Oposto: '))
n2 = float(input('Cateto Adjacente: '))
hi = n1 ** 2 + n2 ** 2
print('A Hipotenusa desse triângulo retângulo é igual a {:.2f}'.format(sqrt(hi)))'''

from math import hypot
n1 = float(input('Cateto Oposto: '))
n2 = float(input('Cateto Adjacente: '))
print('A hipotenusa é igual há {:.2f}!'.format(hypot(n1, n2)))
