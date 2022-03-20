n1 = float(input('Primeira reta: '))
n2 = float(input('Segunda reta: '))
n3 = float(input('Terceira reta: '))
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('Essas retas forrmam um triângulo ', end='')
    if n1 == n2 == n3:
        print('EQUILÁTERO!')
    elif n1 != n2 != n3:
        print('ESCALENO!')
    else:
        print('ISÓSCELES!')
else:
    print('Com essas três retas não é possivel fazer um triângulo!')
