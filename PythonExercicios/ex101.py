def eleição(n):
    from datetime import date
    ano = date.today().year
    idade = ano - n
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA!'
    elif 15 < idade < 18:
        return f'Com {idade} anos: VOTO APICIONAL'
    else:
        return f'Com {idade} anos: VOTO ABRIGATORIO'


n1 = int(input('Em que no você nasceu? '))
print(eleição(n1))
