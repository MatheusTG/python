pr = int(input('Primeiro termo: '))
rz = int(input('Razão: '))
cont = 0
while cont <= 10:
    print(pr, end=' | ')
    pr += rz
    cont += 1
print('FIM')
