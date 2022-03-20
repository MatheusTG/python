n1 = int(input('Digite um número inteiro qualquer: '))
n2 = int(input('Digite mais um número inteiro: '))
if n1 > n2:
    print('\033[1;32mO primeiro valor é maior\033[m!')
elif n1 < n2:
    print('\033[1;32mO segundo valor é maior!\033[m')
else:
    print('\033[1;32mOs dois valores são iguais!\033[m')
