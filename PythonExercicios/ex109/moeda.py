def metade(m=0, formato=False):
    res = m / 2
    return res if not formato else real(res)


def dobro(d=0, formato=False):
    res = d * 2
    return res if not formato else real(res)


def aumentar(a=0, p=0, formato=False):
    res = a + (a / 100 * p)
    return res if formato is False else real(res)


def diminuir(d=0, p=0, formato=False):
    res = d - (d * p / 100)
    return res if not formato else real(res)


def real(preco, real='R$'):
    return f'{real}{preco:.2f}'.replace('.', ',')
