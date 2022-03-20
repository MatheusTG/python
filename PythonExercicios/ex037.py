num = int(input('Digite um número inteiro qualquer: '))
print('''Escolha uma das bases para vonversão:
[ 1 ] Converter para BINÁRIO.
[ 2 ] Converter para OCTAL.
[ 3 ] Converter para HEXADECIAMAL.''')
escolha = int(input('Sua apção: '))
if escolha == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(num, bin(num)[2:]))
elif escolha == 2:
    print('{} convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif escolha == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))
else:
    print('OPCÃO INVALIDA! Tente novamente!')
