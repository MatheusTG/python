c = 'S'
cont = soma = maior = menor = 0
while c in 'Ss':
    n = int(input('Digite um número: '))
    c = str(input('Quer continuar: '))
    soma += n
    cont += 1
    if cont == 1:
        maior = n
        menor = n
    elif n > maior:
        maior = n
    elif n < menor:
        menor = n
media = soma / cont
print('Você digitou {} números e a média foi {:.2f}'.format(cont, media))
print('O maior número que você digitou foi {} e o menor foi {}!'.format(maior, menor))
