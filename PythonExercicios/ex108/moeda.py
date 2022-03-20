def metade(m=0):
    res = m / 2
    return res


def dobro(d=0):
    res = d * 2
    return res


def aumentar(a=0, p=0):
    res = a + (a / 100 * p)
    return res


def diminuir(d=0, p=0):
    res = d - (d * p / 100)
    return res


def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')
