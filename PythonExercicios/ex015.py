km = float(input('Quilômetros percoridos: '))
dias = float(input('Dias alugados: '))
valor = km * 0.15 + dias * 60
print('Você está com uma divida de R${:.2f}'.format(valor))

