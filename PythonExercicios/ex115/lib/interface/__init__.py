def linha(car, tam):
    print(car * tam)


def titulo(txt):
    linha('=-=', 15)
    print(txt.center(44))
    linha('=-=', 15)


def pintar(cor=0, txt='', sin='', c=0, t=''):
    print(f'\033[{cor}m{txt}\033[m', sin,
          f'\033[{c}m{t}\033[m')


def repetir(txt='', erro=''):
    global opc
    while True:
        opc = str(input('\033[33mSua Opção: \033[m'))
        if opc not in erro:
            print(txt)
            continue
        return opc


def sair(msg=''):
    linha('=-=', 15)
    print(msg.center(44))
    linha('=-=', 15)
