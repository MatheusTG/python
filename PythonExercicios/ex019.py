from random import choice
n1 = input('Primeiro aluno: ')
n2 = input('Sugundo aluno: ')
n3 = input('Terceiro aluno: ')
n4 = input('Quarto aluno: ')
lista = (n1, n2, n3, n4)
print('O aluno escolhido foi {}!'.format(choice(lista)))
