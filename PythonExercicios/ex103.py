def jogador(nome='<desconhacido>', gols=''):
    print(f'O jogador {nome.strip()} ', end='')
    if gols != '0' and gols.isnumeric():
        print(f'fez {gols} ', end='')
    else:
        print('0 ', end='')
    print('gol(s) no campeonato!')


jogador(str(input('Qual o nome do jogador? ')),
        str(input('Quantos gols ele fez? ')))
