from datetime import date
anos = date.today().year
carteira = {'nome': str(input('Nome: ')),
            'idade': anos - (int(input('Ano de Nascimento: '))),
            'carteira': int(input('Carteira de trabalho (0 Não tem): '))}
if carteira['carteira'] != 0:
    carteira['contratação'] = int(input('Ano de contratação: '))
    carteira['salario'] = float(input('Salário: R$'))
    carteira['aposentadoria'] = 35 - (anos - carteira['contratação']) + carteira['idade']
print('=-=' * 15)
for k, v in carteira.items():
    print(f'{k} tem o valor {v}')
