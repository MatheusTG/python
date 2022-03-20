n = 0
while True:
    n = int(input('Digite um número, para ver sua tabuada: '))
    print('=' * 40)
    if n < 0:
        print('Esse programa foi interompido por prblemas tecmicos!')
        print('Por favor, tente novamente mais tarde!')
        break
    for c in range(1, 11):
        print(f'{n} x {c} = {n * c}')
    print('=' * 40)
