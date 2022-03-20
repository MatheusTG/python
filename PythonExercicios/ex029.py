speed = int(input('Velocidade do carro: '))
if speed > 80:
    print('Você recebeu uma multa de R${} por estar {}Km/h acima do limite de velocidade!'.format((speed-80)*7, speed-80))
else:
    if speed < 50:
        print('Você recebeu uma multa de R${} por estar {}Km/h abaixo do limite de velocidade!'.format((speed-50)*5, speed-50))
    else:
        print('Tenha um Bom dia, e dirija com segurança!')
