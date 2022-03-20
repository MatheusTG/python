from ex107 import moeda
num = float(input('Digite um número: '))
print(f'A metade de {num} é {moeda.metade(num)}!')
print(f'O dobro de {num} é {moeda.dobro(num)}!')
print(f'Aumentando 10% teremos o valor {moeda.aumentar(num, 10)}')
print(f'Diminuindo 15% teremos o valor {moeda.diminuir(num, 15)}')
