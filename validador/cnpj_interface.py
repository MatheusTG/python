from cnpj_biblioteca import limpar, ultnum, sequencia

cnpj = input('Digite o seu CNPJ: ')
cnpj = limpar(cnpj)
cnpj2 = cnpj[:-2]

multiplica = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

if len(cnpj) == 14:

    num1 = ultnum(cnpj2, multiplica)
    cnpj2 = cnpj2 + num1
    multiplica.insert(0, 6)
    num2 = ultnum(cnpj2, multiplica)

    valor = sequencia(cnpj)

    if cnpj2 + num2 == cnpj and not valor:
        print('O seu CNPJ é valido!')
    else:
        print('O seu CNPJ não é valido!')
else:
    print('Número de caracteres invalido!')
