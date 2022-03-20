from random import randint
vc1 = 1
vc2 = 1
tentativas1 = 0
tentativas2 = 0
num = int(input('Até que número o computador pode pensar? '))
pc = randint(1, num+1)
jogador1 = str(input('\033[34mQuem será jogador 1?\033[m ')).strip().upper()
jogador2 = str(input('\033[31mQuem será jogador 2?\033[m ')).strip().upper()
print('\033[34mVEZ DE {}!\033[m'.format(jogador1))
while pc != vc1:
    vc1 = int(input('Digite um número de 1 a {}: '.format(num)))
    if vc1 > pc:
        print('Menos... Tente outra vez.')
    elif vc1 < pc:
        print('Mais... Tente outra vez.')
    tentativas1 += 1
print('Parabens, você acertou com {} tentativas!'.format(tentativas1))
print('\033[31mVEZ DE {}!\033[m'.format(jogador2))
while pc != vc2:
    vc2 = int(input('Digite um número de 1 a {}: '.format(num)))
    if vc2 > pc:
        print('Menos... Tente outra vez.')
    elif vc2 < pc:
        print('Mais... Tente outra vez.')
    tentativas2 += 1
print('Parabéns, você acertou com {} tentativas!'.format(tentativas2))
if tentativas1 < tentativas2:
    vencedor = jogador1
    pontvencedor = tentativas1
    perdedor = jogador2
    pontperdedor = tentativas2
else:
    vencedor = jogador2
    pontvencedor = tentativas2
    perdedor = jogador1
    pontperdedor = tentativas1
print('\033[32mE O VENCEDOR FOI...\033[m')
print(''
      '{} com apenas {} erros!'.format(vencedor, pontvencedor))
print('CONTRA\n{} com um total de {} erros!'.format(perdedor, pontperdedor))
