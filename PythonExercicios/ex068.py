from random import randint
cont = jogador = 0
print('=-=' * 10)
print('VAMOS JOGAR PAR OU IMPAR')
while True:
    print('=-=' * 10)
    print('Escolha uma opção abaixo!')
    pi = ' '
    while pi not in '12':
        pi = str(input('[ 1 ] IMPAR\n[ 2 ] PAR\nQual você vai ser? '))
    print('=-=' * 10)
    pc = randint(1, 10)
    v = int(input('Diga um valor: '))
    print(f'Você tirou {v} e o compuatador tirou {pc} e a soma de {v} + {pc} = {v + pc}', end='')
    print(', Deu par' if (pc + v) % 2 == 0 else ', Deu impar')
    if pi == '2' and (pc + v) % 2 == 1 or pi == '1' and (pc + v) % 2 == 0:
        print('\033[31mVocê perdeu!\033[m')
        break
    else:
        print('\033[32mVocê venceu!\033[m')
        cont += 1
print(f'Você teve {cont} vitorias consecutivas!')
