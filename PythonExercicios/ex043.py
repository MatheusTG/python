peso = float(input('Qual o seu peso? '))
altura = float(input('Qual a sua altura? '))
imc = peso / (altura * altura)
if imc < 18.5:
    print('Você está abaixo do peso!')
elif 18.5 <= imc < 25:
    print('Você está no peso ideal!')
elif 25 <= imc < 30:
    print('Você está com Sobrepeso!')
elif 30 <= imc < 40:
    print('Você está com plobremas de OBESIDADE!')
else:
    print('Você esta com OBESIDADE MÓRBIDA, Cuidado!')
