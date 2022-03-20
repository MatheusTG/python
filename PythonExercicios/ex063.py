termos = int(input('quantos termos você quer monstrar? '))
n1 = 0
n2 = 1
print('| {} | {}'.format(n1, n2), end='')
cont = 3
while cont <= termos:
    n3 = n1 + n2
    print(' | {}'.format(n3), end='')
    cont += 1
    n1 = n2
    n2 = n3
print(' | FIM')
