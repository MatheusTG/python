princ = list()
while True:
    n1 = str(input('Nome: '))
    n2 = float(input('Nota 1: '))
    n3 = float(input('Nota 2: '))
    princ.append([n1, [n2, n3], (n2 + n3) / 2])
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Você quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print('=-=' * 10, '\nN°  NOME           MÉDIA')
for p, v in enumerate(princ):
    print(f'{p}   {v[0]:<15}{v[2]:.1f}')
print('=-=' * 10)
perg = 0
while True:
    perg = int(input('Monstrar as notas de qual aluno? (999 Interonpe): '))
    if perg < 999 and perg <= len(princ) - 1:
        print('_' * 30, f'\nAs notas de {princ[perg][0]} são: {princ[perg][1]}\n', '_' * 30)
    elif perg == 999:
        print('=-=' * 17)
        print(' ' * 10, '<<<| VOLTE SEMPRE |>>>')
        print('=-=' * 17)
        break
    elif perg > len(princ):
        print('Valor invalido, tente novamente!')
