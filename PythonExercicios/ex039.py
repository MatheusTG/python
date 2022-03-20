from datetime import date
print('Você é de que genero?')
print('[ 1 ] Masculino.\n[ 2 ] Feminino.')
genero = int(input('Genero: '))
if genero == 2:
    print('Você não é obrigada a se alistar mas, caso queira:')
    print('[ 0 ] Não quero me alistar!\n[ 1 ] Quero me alistar!')
    escolha = int(input('Sua escolha: '))
    if escolha == 0:
        print('Caso mude de ideia entre em contato!')
    elif escolha == 1:
        print('BLZ, Então me diga:')
        nasc = int(input('Em que ano você nasceu? '))
        idade = date.today().year - nasc
        if idade < 18:
            print('Falta {} anos para você se alistar para o exercito!'.format(18 - idade))
            print('O ano do alistamento será {}'.format(18 - idade + date.today().year))
        elif idade == 18:
            print('Você já pode se alistar, pois já compretou 18 anos!')
        elif idade > 18:
            print('Já passou {} da sua data de alistamento então vá o mais rapido possivel!'.format(idade - 18))
    else:
        print('Opção invalida. Tente novamente!')
elif genero == 1:
    nasc = int(input('Em que ano você nasceu? '))
    idade = date.today().year - nasc
    if idade < 18:
        print('Falta {} anos para você se alistar para o exercito!'.format(18 - idade))
        print('O ano do alistamento será {}'.format(18 - idade + date.today().year))
    elif idade == 18:
        print('Então CORRE porque já chegou a hora!')
    elif idade > 18:
        alist = str(input('Você já se alistou para o exercito? ')).upper().strip()
        if alist == 'NÃO' or alist == 'NAO' and idade > 18:
            print('VAI LOGO ENTÃO!!! Porque já passou {} anos que você fez 18!!!'.format(idade - 18))
        elif alist == 'SIM':
            legal = str(input('Foi legal? ')).upper().strip()
            if legal == 'SIM' or 'FOI':
                print('Ainda bem!')
            elif legal == 'NÃO' or legal == 'NAO':
                print('Que chato!')
            else:
                print('Desculpe não entendi, por favor, tente novamente!')
        else:
            print('Opcão invalida. Tente novamente!,')
else:
    print('Opção invalida. Tente novamente!.')
