import re


def limpar(nums=''):
    return re.sub(r'[^0-9]', '', nums)


def ultnum(cnpj, multiplica):
    soma = 0
    for p, v in enumerate(multiplica):
        soma += int(cnpj[p]) * v
    pd = 11 - (soma % 11)
    if pd > 9:
        pd = 0
    return str(pd)


def sequencia(cnpj):
    if cnpj[0] * len(cnpj) == cnpj:
        return True
    else:
        return False