jogador = dict()
temp = list()
time = list()
while True:
    jogador['nome'] = str(input('Nome do jogador: '))
    jogos = int(input(f'Quantos jogos {jogador["nome"]} jogou? '))
    for c in range(jogos):
        temp.append(int(input(f'Quantos gols na {c + 1}° partida? ')))
    jogador['gols'] = temp.copy()
    jogador['total'] = sum(temp)
    time.append(jogador.copy())
    jogador.clear(), temp.clear()
    while True:
        c = str(input('Você deseja cadastrar mais um jogador? [S/N] ')).strip().upper()[0]
        if c in 'SN':
            break
        print('Por favor digite penas S ou N!')
    if c == 'N':
        break
print('N° NOME           GOLS          TOTAL')
for p, v in enumerate(time):
    print(f'{p + 1}', end='  ')
    for dado in v.values():
        print(f'{str(dado):<15}', end='')
    print()
while True:
    dados = int(input('Monstrar dados de qual jogador? (999 para parar): '))
    if dados == 999:
        break
    if dados > len(time) or dados < 1:
        print(f'Erro, não existe jogador {dados}!')
    else:
        print(f'===== Levantamento do jogador {time[dados - 1]["nome"]} =====')
        for d in range(len(time[dados - 1]["gols"])):
            print(f'No jogo {d + 1} fez {time[dados -1]["gols"][d]} gols!')
print('<<< VOLTE SEMPRE >>>')
