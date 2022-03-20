#Forma simprificada
'''viajem = float(input('Qual a distancia da sua viajem? '))
print('Você está prestes a começar uma viajem de {}!'.format(viajem))
valor = viajem * 0.45 if viajem >= 200 else viajem * 0.50
print('Sua viajem custará R${}!'.format(valor))'''

viajem = float(input('Qual a distancia da sua viajem? '))
if viajem >= 200:
    print('Sua viajem cuatará R${}!'.format(viajem * 0.45))
else:
    print('Sua viajem custará R${}!'.format(viajem * 0.50))
