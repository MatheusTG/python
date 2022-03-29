salario = int(input('Digite o seu salário: '))

if salario < 1000:
    print(f"O valor do seu salário reajustado é de R$: {salario * 1.30}")

else:
    print("Desculpe, mas você não tem direito ao reajuste!")
