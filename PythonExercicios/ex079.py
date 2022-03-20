lista = []
while True:
    num = int(input('Digite um número: '))
    if num not in lista:
        print('Valor adicionado com sucesso!')
        lista.append(num)
    else:
        print('Valor duplicado! NÃO foi adicionado!!!')
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Você quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        print(f'Você adicionou os valores {sorted(lista)}')
        break
