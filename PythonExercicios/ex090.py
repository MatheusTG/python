dicionario = {'Nome': str(input('Nome: ')), 'Media': float(input('Média: '))}
if dicionario['Media'] >= 7.0:
    dicionario['Situação'] = 'APROVADO'
elif 5 <= dicionario['Media'] < 7:
    dicionario['Situação'] = 'RECUPERAÇÃO'
else:
    dicionario['Situação'] = 'REPROVADO'
for k, v in dicionario.items():
    print(f'{k} igual a {v}')
