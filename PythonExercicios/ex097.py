def escreva(*n):
    tam = len(n[0]) + 4
    print('=' * tam)
    print(f'  {n[0]}')
    print('=' * tam)


escreva(f'{"Matheus":^15}')
escreva(f'{"Meu nome é Matheus e o da minha irmã é Isabela"}')
