valor1 = float(input("Digite um número positivo: "))
valor2 = float(input("Digite outro número positivo: "))
print()

print("""Escolha uma das opções a baixo: 
[ 1 ] Média entre os números digitados
[ 2 ] Diferença do maior pelo menor
[ 3 ] Produto entre os números digitados
[ 4 ] Divisão do primeiro pelo segundo""")
escolha = input("Qual a sua escolha: ")

print()
if escolha == '1':
    print(f"A média entre os númeos digitados é de {(valor1 + valor2) / 2}!")

elif escolha == '2':
    if valor1 > valor2:
        print(f"A diferença entre os dois é de {valor1 - valor2}!")
    else:
        print(f"A diferença entre os dois é de {valor2 - valor1}!")

elif escolha == '3':
    print(f"O produto entre os dois números digitados é de {valor1 * valor2}!")

elif escolha == '4':
    if valor2 == '0':
        print("Desculpe, mas segundo valor não pode ser zeno na opção 4!")

    else:
        print(f"A divisão do primeiro pelo segundo é de {valor1 / valor2:.2f}!")

else:
    print("Essa opção não é valida, por favor tente novamente!")
