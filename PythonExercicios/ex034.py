sal = float(input('Qual o valor do seu salario? '))
if sal > 1250:
    print('Você recebou um aumento de 10%, agora seu salario e de {}'.format(sal + (sal/100*10)))
else:
    print('Você recebeu um aumento de 15%, agora seu salario é de {}!'.format(sal + (sal*15/100)))
