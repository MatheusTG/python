def área(l, c):
    print(f'A área desse terreno {l} x {c} é de {l * c}m²')


print(f'=====| Controle de terrenos |=====\n{"=-=" * 11}')
área(float(input('Largura: (Em metros!): ')),
     float(input('Comprimrnto: (Em metros!): ')))
print('=-=' * 11)
