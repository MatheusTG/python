partidas = list()
fuut = {'nome': str(input('Qual o nome do jogador? '))}
tot = int(input(f'Quantas partidas {fuut["nome"]} jogou? '))
for c in range(1, tot + 1):
    partidas.append(int(input(f'Quantos gols na partida {c}? ')))
fuut['gols'] = partidas[:]
fuut['total'] = sum(partidas)
print('=-=' * 20, f'\nDicionario: {fuut}')
print('=-=' * 20)
for k, v in fuut.items():
    print(f'O campo {k} tem valor {v}')
print('=-=' * 20)
print(f'O jogador {fuut["nome"]} jogou {tot} partidas.')
cont = 0
for c in range(len(fuut['gols'])):
    cont += 1
    print(f'     => Na partida {cont}, fez {fuut["gols"][cont - 1]} gols.')
print(f'Foi um total de {fuut["total"]} gols.')
