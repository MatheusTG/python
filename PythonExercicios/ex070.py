from time import sleep
print('======= CALCULE O VALOR DA SUA COMPRA! =======0')
soma = mais1000 = barato = cont = nome = 0
while True:
    c = str(input('Qual o nome do seu produto? '))
    p = float(input('Preço: R$ '))
    while True:
        m = str(input('Você deseja comprar mais produtos? [S/N]: ')).upper()[0]
        if m in 'SsNn':
            break
    soma += p
    cont += 1
    if p > 1000:
        mais1000 += 1
    if cont == 1 or p < barato:
        barato = p
        nome = c
    if m == 'N':
        break
print('CALCULANDO...')
sleep(2)
print(f'O gasto total dessa compra é de R${soma:.2f}')
print(f'Nessa compra {mais1000} produtos custam mais de R$1000,00')
print(f'O nome do produto mais barato é {nome}, e o preço de dele é R${barato:.2f}!')
