from ex109 import moeda
num = float(input('Digite um número: R$'))
print(f'A metade de {moeda.real(num)} é {moeda.metade(num, formato=True)}')
print(f'O dobro de {moeda.real(num)} é {moeda.dobro(num, formato=True)}')
print(f'Aumentando 10% teremos o valor {moeda.aumentar(num, 10, formato=True)}')
print(f'Diminuindo 13% teremos o valor {moeda.diminuir(num, 13, formato=True)}')
