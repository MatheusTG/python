from random import randint
from time import sleep
from operator import itemgetter
dados = {'jogador1': randint(1, 6), 'jogador2': randint(1, 6),
         'jogador3': randint(1, 6), 'jogador4': randint(1, 6)}
for k, v in dados.items():
    print(f'O {k} tirou {v}')
    sleep(0.5)
ranking = sorted(dados.items(), key=itemgetter(1), reverse=True)
print('=-=' * 15)
print(' ' * 10, 'RANKING DOS JOGADORES')
print('=-=' * 15)
for i, v in enumerate(ranking):
    print(f'{i + 1}° Lugar: {v[0]} com {v[1]} pontos')
    sleep(0.5)
print('=-=' * 15)
