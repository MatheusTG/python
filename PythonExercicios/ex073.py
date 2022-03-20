times = ('Palmeiras', 'Flamengo', 'Internacional', 'Grêmio',
         'São Paulo', 'Atlético-MG', 'Athletico-PR', 'Cruzeiro',
         'Botafogo', 'Santos', 'Bahia', 'Fluminense', 'Corinthians',
         'Chapecoense', 'Ceará', 'Vasco', 'Sport', 'América-MG', 'Vitória Paraná')
print('\033[31m=-=\033[m' * 10)
print(f'Lista dos times do Brasileirão: {times}')
print('\033[31m=-=\033[m' * 10)
print(f'Os 5 primeiros colocados do Brasileirão são: {times[:5]}')
print('\033[31m=-=\033[m' * 10)
print(f'Os 4 ultimos colocados do Brasileirão são: {times[-4:]}')
print('\033[31m=-=\033[m' * 10)
print(f'Times em ordem alfabetica: {(sorted(times))}')
print('\033[31m=-=\033[m' * 10)
print('O time da Chapecoense está em {}° Lugar, no Brasleirão!'.format(times.index('Chapecoense')+1))
print('\033[31m=-=\033[m' * 10)
