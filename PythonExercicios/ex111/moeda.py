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


def resumo(num=0, dim=5, aum=10):
    print('=-=' * 13,)
    print('RESUMO DO VALOR'.center(38))
    print('=-=' * 13,
          f'\n ==> Preço analizado: \t{real(num)}',
          f'\n ==> Metade do preço: \t{metade(num, formato=True)}',
          f'\n ==> Dobro do preço: \t{dobro(num, formato=True)}',
          f'\n ==> {dim}% de redução: \t{diminuir(num, dim, formato=True)}',
          f'\n ==> {aum}% de aumento: \t{aumentar(num, aum, formato=True)}')
    print('=-=' * 13)
