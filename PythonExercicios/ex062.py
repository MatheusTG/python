pr = int(input('Primeiro termo: '))
rz = int(input('Razão: '))
termo = pr
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print(termo, end=' | ')
        termo += rz
        cont += 1
    print('PAUSA')
    mais = int(input('Você quer mais quantos termos? '))
print('Essa PA foi finalizada com {} termos!'.format(total))
