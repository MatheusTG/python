frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra A apareceu {} vezes na frase!'.format(frase.count('A')))
print('A primeira letra A aperaceu na posição {}.'.format(frase.find('A')+1))
print('A ultima letra letra A aperece na posicão {}.'.format(frase.rfind('A')))
