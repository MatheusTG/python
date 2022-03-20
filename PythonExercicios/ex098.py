def contador(a, b, c):
    def linha():
        print('=-=' * 10)
    from time import sleep
    linha()
    cont = a
    if c < 0:
        c *= -1
    if c == 0:
        c = 1
    if a <= b:
        print(f'Contagem de {a} até {b} de {c} em {c}:')
        while cont <= b:
            print(f'{cont} ', end=''), sleep(0.25)
            cont += c
    elif a > b:
        print(f'Contagem de {a} até {b} de {c} em {c}:')
        while cont >= b:
            print(f'{cont}', end=' '), sleep(0.25)
            cont -= c
    print('Fim!')


contador(1, 10, 1)
contador(10, 0, 2)
print('=-=' * 10)
print('Agora é a sua vez de personalizar a contagem!')
while True:
    contador(int(input('Início: ')),
             int(input('Fim:    ')),
             int(input('Passo:  ')))
    while True:
        continuar = str(input('Você quer continuar? [S/N] ')).strip().upper()[0]
        if continuar in 'SN':
            break
    if continuar == 'N':
        break
print('<<< VOLTE SEMPRE >>>')
