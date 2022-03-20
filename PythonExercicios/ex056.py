somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = 0
contagem = 0
for c in range(1, 5):
    print('______{}° PESSOA ______'.format(c))
    nome = str(input('Qual o seu nome? ')).strip()
    idade = int(input('Qual a sua idade? '))
    genero = str(input('Qual o seu genero [M/F]? ')).strip()
    somaidade += idade
    if c == 1 and genero in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if genero in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if genero in 'Ff' and idade < 20:
        contagem += 1
mediaidade = somaidade / 4
print('A media de idade das pessoas desse grupo é de {}!'.format(mediaidade))
print('O homem mais velho do grupo tem {} e se chama {}!'.format(maioridadehomem, nomevelho))
print('Nesse grupo a {} molheres com menos de 20 anos:'.format(contagem))
