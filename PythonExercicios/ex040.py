n1 = float(input('Qual foi sua nota na primeira prova? '))
n2 = float(input('Qual foi sua nota na segunda prova? '))
media = (n1 + n2) / 2
if media < 5.0:
    print('Sua media foi {} então você foi \033[1;31mREPROVADO!\033[m'.format(media))
elif media > 7.0:
    print('Sua media foi {} então você foi \033[1;32mAPROVADO!\033[m'.format(media))
elif 5.0 < media <= 7.0:
    print('Sua media foi {} então você está de \033[1;33mRECUPERAÇÃO!\033[m'.format(media))
