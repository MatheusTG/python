def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric() or n[1:].isnumeric() and n[0] == '-':
            valor = int(n)
            ok = True
        else:
            print('\033[31mERRO! Digite apenas um valor numérico valido!\033[m')
        if ok:
            break
    return valor


n1 = leiaInt('Digite um número: ')
print(f'Você digitou o valor {n1}')
