def leiadinheiro(n):
    teste = list()
    valido = False
    while not valido:
        num = str(input(n)).replace(',', '.').strip()
        for c in num:
            if c.isalpha():
                teste.append(c)
        if num.isalpha() or num == '' or len(teste) > 0:
            print(f'\033[31mERRO, \'{num}\' não é um valor valido!\033[m')
        else:
            valido = True
            return float(num)
