'''print('=-=' * 12)
print(' ' * 9, 'BANCO DO BRASIL')
print('=-=' * 12)
valor = int(input('Quanto você deseja sacar? R$'))
cont50 = valor // 50
r50 = valor % 50
r20 = valor % 20
if valor < 50:
    cont20 = valor // 20
else:
    cont20 = r50 // 20
cont10 = 0
conta = (valor - (cont50 * 50 + cont20 * 20))
if conta >= 10:
    cont10 = conta // 10
cont01 = valor % 10
if cont50 > 0:
    print(f'Total de {cont50} cédulas de R$50')
if cont20 > 0:
    print(f'Total de {cont20} cédulas de R$20')
if cont10 > 0:
    print(f'Total de {cont10} cédulas de R$10')
if cont01 > 0:
    print(f'Total de {cont01} cédelas de R$1')'''

valor = int(input('Qual valor você deseja sacar? R$'))
cont50 = nota50 = 0
while True:
    cont50 = valor - 50
