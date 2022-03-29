lado1 = int(input("Digite o lado 1: "))
lado2 = int(input("Digite o lado 2: "))
lado3 = int(input("Digite o lado 3: "))

if lado1 == lado2 and lado2 == lado3:
    print("Esse triângulo é EQUILÁTERO!")

elif lado1 != lado2 and lado2 != lado3 and lado1 != lado3:
    print("Esse triângulo é ESCALENO!")

else:
    print("Esse triângulo é ISÓCELES!")
