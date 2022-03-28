idade = input('Digite sua idade em ANOS, MESES E DIAS usando uma virgula para separar: ')
lista = idade.split(',')
print(f"Idade em dias: {int(lista[0].strip()) * 365 + int(lista[1].strip()) * 30 + int(lista[2].strip())}")
