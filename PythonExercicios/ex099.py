def num(*c):
    def linha():
        print('=-=' * 20)
    linha(), print('Analisando os valores passados...')
    cont = maior = 0
    for v in c:
        print(v, end=' ')
        if cont == 1 or v > maior:
            maior = v
    print(f'Foram informados {len(c)} valores!', end='')
    print(f'\nO maior valor informado foi {maior}.')
    cont += 1


num(2, 7, 4, 0, 5, 2), num(8, 4, 7), num(9, 2), num(5), num(), print('=-=' * 20)
