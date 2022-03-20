print('\033[1;34mConpre sua casa no nossao site!\033[m')
casa = float(input('Qual o valor da casa que você deseja? R$'))
sal = int(input('Qual o valor do seu salário? '))
ano = int(input('Em quantos anos deseja pagar? '))
if casa / ano / 12 < sal / 100 * 30:
    print('Parabéns o seu emprestimo foi \033[32mAPROVADO!\033[m'.format(casa/ano/12))
    print('A prestação ficou em R${:.2f} Mensais!'.format(casa/ano/12))
else:
    print('\033[1;31mINFELISMENTE\033[m seu pedido não foi aprovado!')
