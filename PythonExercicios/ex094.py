temp = dict()
cadastro = list()
soma = cont = contv = 0
while True:
    temp['nome'] = str(input('Nome: '))
    while True:
        g = str(input('Genero: [M/F] ')).strip().upper()[0]
        temp['genero'] = g
        if g in 'MF':
            break
        print(f'Caracter invalido, por favor digite apenas M ou F!')
    temp['idade'] = int(input('Idade: '))
    soma += temp['idade']
    cadastro.append(temp.copy())
    temp.clear()
    while True:
        continuar = str(input('Deseja cadastrar mais alguém? [S/N] ')).strip().upper()[0]
        if continuar in 'SN':
            break
        print(f'Caracter invalido, por favor digite apenas S ou N!')
    if continuar == 'N':
        break
print('=-=' * 15, f'\n   ==> Ao todo temos {len(cadastro)} pessoas cadastradas!')
print(f'   ==> A média de idade dessas pessoas é de {soma / len(cadastro)} idade!')
print(f'   ==> As molheres cadastradas foram / ', end='')
for p, v in enumerate(cadastro):
    if cadastro[p]['genero'] == 'F':
        print(f'{v["nome"]} / ', end='')
print('\n====== Lista de pessoas que estão acima da média! ======')
for p, v in enumerate(cadastro):
    if cadastro[p]['idade'] > soma / len(cadastro):
        cont += 1
        print(f'    {cont}° Pessoa: nome = {cadastro[p]["nome"]}; ', end='')
        print(f'genero = {cadastro[p]["genero"]}; ', end='')
        print(f'idade = {cadastro[p]["idade"]}')
