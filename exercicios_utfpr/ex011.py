from tkinter import Y


x = input("Digite a variável X: ")
y = input("Digite a variável Y: ")

z = x
x = y
y = z

print(f"Os valores trocados de X e Y são respectivamente: {x} e {y}")
