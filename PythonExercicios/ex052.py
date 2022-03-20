tot = 0
n = int(input('Digite um número inteiro: '))
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[34m', end=' ')
        tot += 1
    else:
        print('\033[m', end=' ')
    print(c, end=' ')
if tot == 2:
    print('\n\033[mEsse número é primo!')
else:
    print('\n\033[mEsse número não é primo!')
