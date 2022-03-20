temp = list()
princ = list()
cont = menor = maior = 0

while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))

    if len(princ) == 0:
        menor = maior = temp[1]
    elif temp[1] < menor:
        menor = temp[1]
    elif temp[1] > maior:
        maior = temp[1]
    princ.append(temp[:])
    temp.clear()

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar in 'N':
        break

print()
print(f'Ao todo você cadastrou {len(princ)} pessoas!')
print(f'O menor peso foi {menor}Kg e foi das pessoas: ', end='')
for c in princ:
    if c[1] == menor:
        print(f'{c[0]}... ', end='')
print(f'\nO maior peso foi {maior}Kg e foi das pessoas: ', end='')
for c in princ:
    if c[1] == maior:
        print(f'{c[0]}... ', end='')
