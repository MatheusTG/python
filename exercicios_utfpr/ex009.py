idade = input("Digite sua idade em ANOS, MESES E DIAS usando uma virgula para separar: ")
lista = idade.split(',')

print(f"Idade em dias: {int(lista[0].strip()) * 365 + int(lista[1].strip()) * 30 + int(lista[2].strip())}")



idade_ano = int(input("Quantos anos você tem? "))
idade_mes = input("Quantos mêses você tem? ")
idade_dia = input("Quantos dias você tem? ")

print(f"A sua idade em DIAS é igual a {idade_ano * 365 + idade_mes * 30 + idade_dia}")
