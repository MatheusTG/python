genero = str(input('Informe se genero?[M/F]: ')).strip().upper()[0]
while genero not in 'MmFf':
    genero = str(input('Dados invalidos. Por favor, informe seu genero: ')).strip().upper()[0]
if genero in 'Mm':
    print('Gerero MASCULINO registrado com sucesso!')
elif genero in 'Ff':
    print('Genero FEMININO registrado com sucesso!')
