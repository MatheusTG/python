from datetime import date
ano = int(input('Em que ano o nadador nasceu? '))
idade = date.today().year - ano
if idade < 9:
    print('Esse nadador é da categoria \033[1;33mMIRIM!\033[m')
elif idade <= 14:
    print('Esse nadador é da categoria \033[1;33mINFANTIL!\033[m ')
elif idade <= 19:
    print('Esse nadador é da categoria \033[1;33mJUNIOR!\033[m')
elif idade <= 25:
    print('Esse nadador é da categoria \033[33mSÉNIOR\033[m')
else:
    print('Esse nadador é da categoria \033[1;33mMASTER!\033[m')
