n1 = float(input('Primeira reta: '))
n2 = float(input('Segunda reta: '))
n3 = float(input('Terceira reta: '))
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('Sim, é possivel fazer um triângulo com essas três retas!')
else:
    print('Não é possivel fazer um triângulo com essas três retas: ')
