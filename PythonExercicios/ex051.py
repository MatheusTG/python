n1 = int(input('Qual o primeiro termo da PA? '))
n2 = int(input('Qual a Razão da PA? '))
print('Os 10 primeiros termos dessa progressão são:')
for c in range(n1, n2*10 + n1, n2):
    print(c, end=' | ')
