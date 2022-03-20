from random import randint
from time import sleep
n1 = randint(1, 3)
print('-=-' * 20)
print('              \033[1;34mADIVINHE OQUE ESTOU PENSANDO\033[m')
print('-=-' * 20)
n2 = int(input('Digite um número DE 1 a 3: '))
print('\033[1;33mPROCESSANDO...\033[m')
sleep(2)
if n1 == n2:
    print('=' * 30, '\n \033[1;32mPARABÉNS, Você ACERTOU!\033[m')
    print('=' * 30)
else:
    print('=' * 45)
    print('\033[1;31mERROU, Mas não desanime, Tente novamente!\033[m'.format(n1))
    print('=' * 45)
    print('O número que eu tinha pensado era o {}!'.format(n1))
print()
print('Versão so Jogo 1.3')
