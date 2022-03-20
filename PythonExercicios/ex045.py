from time import sleep
from random import randint
while True:
    listacomputador = ('Pedra', 'Papel', 'Tesoura')
    listajogada = ('Opção invalida, tente novamente', 'Pedra', 'Papel', 'Tesoura')
    print('\033[36mEscolha uma das opções abaixo!\033[m')
    print('[ 1 ] Pedra\n[ 2 ] Papel\n[ 3 ] Tesoura')
    jog = int(input('Qual sua jogada: '))
    print('\033[34mJO\033[m')
    sleep(0.5), print('\033[31mKEN\033[m')
    sleep(0.5), print('\033[33mPO!!!\033[m')
    sleep(0.3)
    comp = randint(0, 2)
    print('=' * 30)
    print('Você: {}'.format(listajogada[jog]))
    print('Computador: {}'.format(listacomputador[comp]))
    print('=' * 30)
    if comp == 0 and jog == 3 or comp == 1 and jog == 1 or comp == 2 and jog == 2:
        print('\033[31mHAHA! EU GANHEI!\033[m')
    elif comp == 0 and jog == 2 or comp == 1 and jog == 3 or comp == 2 and jog == 1:
        print('\033[32mPARABÉS Você ganhou!\033[m')
    else:
        print('\033[33mEMPATE!\033[m')
