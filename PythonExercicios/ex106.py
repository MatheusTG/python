def ajuda():
    from time import sleep
    cores = ('\033[m',
             '\033[41m')
    def titulo(txt, cor):
        tam = len(txt) + 4
        print(cores[cor], end='')
        print('~' * tam)
        print(f'  {txt}')
        print('~' * tam)
        print(cores[0])
    titulo('Matheus', 1)
    while True:
        print('\033[30:43m''~' * 30, '\n   SISTEMA DE AJUDA PyHELP')
        print('~' * 30, ' ' * 90, '\033[m')
        n1 = str(input('Função ou Biblioteca > ')).strip()
        if n1.upper() == 'FIM':
            print('\033[41:2m''~' * 20, '\n  ATÉ LOGO!')
            print('~' * 20, ' ' * 100, '\033[m')
            break
        print('\033[30:42m''~' * 50, f'\n   Acessando manual de comando {n1}...')
        print('~' * 50, ' ' * 90, '\033[m', '\033[31:40m')
        sleep(1)
        help(f'{n1}')


ajuda()
