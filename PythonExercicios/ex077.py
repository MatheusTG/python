tupla = ('Quando', 'Aprender', 'Programar', 'Ficarei', 'Muito', 'Rico',
         'Estarei', 'Trabalhando', 'Cheio', 'Felicidade')
for p in tupla:
    print(f'\nNa palavra {p.upper()} temos: ', end='')
    for l in p:
        if l.lower() in 'aeiou':
            print(f'{l}', end=' ')
