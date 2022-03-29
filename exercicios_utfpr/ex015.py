hora_trabalho = int(input("Digite o número de horas trabalhadas: "))
salario_min = int(input("Digite o valor do salario minímo: "))
horaextra = int(input("Digite o número de horas extras trabalhadas: "))

print(f"A salario é igual a R$: {salario_min / 8 * hora_trabalho + salario_min / 4 * horaextra}")
