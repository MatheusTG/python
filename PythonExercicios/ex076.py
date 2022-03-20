compras = ('Arroz', 10.89, 'Feijão', 8.76, 'Tomate', 4.32,
           'Sal', 3.50, 'Farinha', 6.43, 'Guarana', 3.43,
           'Batata', 5.40, 'Detergente', 2.30, 'Maionese', 4.60)
print('=-=' * 13)
print(f'{"LISTAGEM DE PREÇOS":^37}')
print('=-=' * 13)
for c in range(0, len(compras)):
    if c % 2 == 0:
        print(f'{compras[c]:.<30}R$ {compras[c+1]:5.2f}')
