continuar = ''
mais18 = homens = molheres20 = 0
while continuar in 'Ss':
    print('=' * 35)
    print('       CADASTRE UMA PESSOA')
    print('=' * 35)
    idade = int(input('Idade: '))
    genero = str(input('Genero: [M/F] ')).upper()[0]
    if genero not in 'MmFf':
        genero = str(input('Genero: [M/F] ')).upper()[0]
    print('=' * 35)
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Você quer continuar?[S/N] ')).upper()[0]
    if idade >= 18:
        mais18 += 1
    if genero == 'M':
        homens += 1
    if genero == 'F' and idade < 20:
        molheres20 += 1
print('======= FIM DO PROGRAMA! =======')
print('Total de pessoas com mais de 18 anos: {}'.format(mais18))
print('Total de homens cadastrados: {}'.format(homens))
print('Total de molheres com menos de 20 anos: {}'.format(molheres20))
