dec = 0
n1 = int(input('Digite um número: '))
n2 = int(input('Digite mais um número: '))
while dec != 5:
    print('Escolha uma das apções abaixo: ')
    print('[ 1 ] Somar\n[ 2 ] Multiplicar\n[ 3 ] Maior\n[ 4 ] Novos números\n[ 5 ] Sair do programa')
    dec = int(input('Sua decisão: '))
    if dec == 1:
        soma = n1 + n2
        print('Soma = {}'.format(soma))
    elif dec == 2:
        mult = n1 * n2
        print('multiplicação = {}'.format(mult))
    elif dec == 3:
        if n1 > n2:
            maior = n1
            print('Maior = {}'.format(maior))
        else:
            maior = n2
            print('Maior = {}'.format(maior))
    elif dec == 4:
        n1 = int(input('Digite um número: '))
        n2 = int(input('Digite mais um número: '))
    elif dec == 5:
        print('Foi bom trabalhar com você!')
    else:
        print('Esse número não está entre as opções acima. Por favor, tente novamente!')
