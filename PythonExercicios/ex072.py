tupla = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete',
         'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Catorze', 'Quinze',
         'Dezesseis', 'Dezesete', 'Desoito', 'Dezenove', 'Vinte')
cont = 0
while True:
    c = int(input('Digite um número de 0 a 20: '))
    if -1 < c <= 20:
        print(f'O número que você digitou foi {tupla[c]}!')
        cont = ' '
        while cont not in 'SN':
            cont = str(input('Você quer continuar? [S/N] ')).strip().upper()[0]
            if cont not in 'SN':
                print('Tente novamente. ', end='')
    if cont in 'N':
        print('Foi bom trabalhar com você!')
        break
    else:
        print('Tente novamente!', end=' ')
