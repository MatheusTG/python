def leiaint(txt):
    num = 0
    while True:
        try:
            num = int(input(txt))
        except (ValueError, TypeError):
            print('\033[31mERRO, por favor digite um número inteiro valido!\033[m')
            continue
        return num


def leiafloat(txt):
    num = 0
    while True:
        try:
            num = float(input(txt))
        except (ValueError, TypeError):
            print(f'\033[31mERRO, por favor digite um número inteiro valido!\033[m')
            continue
        return num


Int = leiaint('Digite um valor INTEIRO: ')
Float = leiafloat('Digite um valor REAL: ')
print(f'O valor inteiro digitado foi {Int} e o alor real foi {Float}!')
