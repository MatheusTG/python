print('{:-^50}'.format('Calcule o valor da sua compra!'))
valor = float(input('Qual o valor do seu produto? R$'))
print('Como você deseja pagar esse produto?')
print('[ 1 ] À vista no boleto\n[ 2 ] À vista no catão')
print('[ 3 ] 2x no cartão\n[ 4 ] 3x ou mais no cartão')
pagamento = int(input('Escolha oque seja melhor para você: '))
if pagamento == 1:
    print('Seu produto custará {:.2f}!'.format(valor - (valor/100*10)))
elif pagamento == 2:
    print('Seu produto custará {:.2f}!'.format(valor - (valor/100*5)))
elif pagamento == 3:
    print('Seu produto custará {:.2f}!'.format(valor))
    print('Divididos em duas parcelas de {:.2f}, sem juros!'.format(valor/2))
elif pagamento == 4:
    parcelas = int(input('Em quantas parcelas deseja pagar? '))
    print('Seu produto custará {:.2f}!'.format(valor + (valor/100*20)))
    print('Divididos em {} vezes de R${:.2f}, com juros de 20%!'.format(parcelas, (valor+valor/100*20)/parcelas))
else:
    print('Esse valor não é valido. Por favor tente novamente!')
