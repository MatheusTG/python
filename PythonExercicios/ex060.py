'''from math import factorial
n1 = int(input('Digite um número: '))
fatorial = factorial(n1)
print('A FATORIAL de {} é {}!'.format(n1, fatorial))'''

n = int(input('Digite um número: '))
c = n
f = 1
while c > 0:
    print('{}'.format(c), end=' ')
    print('x' if c > 1 else '=', end=' ')
    f *= c
    c -= 1
print(f)

'''n = int(input('Digite um número: '))
c = n
f = 1
for j in range(1, n+1):
    print('{}'.format(c), end=' ')
    print('x' if c > 1 else '=', end=' ')
    f *= c
    c -= 1
print(f)'''
