nota1 = float(input("Digite sua 1º nota escolar: "))
nota2 = float(input("Digite sua 2º nota escolar: "))

media = (nota1 + nota2) / 2

if media >= 6:
    print(f"Sua média é de {media}, e por isso você está APROVADO!")

elif media < 3:
    print(f"Sua média é de {media}, e por isso você está REPROVADO!")

else:
    print(f"Sua média é de {media}, e por isso você está de RECUPERAÇÃO!")
