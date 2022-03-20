from random import randint
from time import sleep
palp = list()
jogos = list()
palpites = 0
sort = int(input('Quantos jogos você quer que eu sortei? '))
for c in range(0, sort):
    while len(palp) < 6:
        r = randint(1, 60)
        if r not in palp:
            palp.append(r)
        palp.sort()
    jogos.append(palp[:])
    palp.clear()
for p, v in enumerate(jogos):
    print(f'jogo {p+1}: {v}')
    sleep(1)
print('==-==-==-== < BOA SORTE > ==-==-==-==')
