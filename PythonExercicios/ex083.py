nuns = str(input('Digite uma expressão que use parênteses: '))
lista = list()
for simb in nuns:
    if simb == '(':
        lista.append(simb)
    elif simb == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista. append(')')
            break
if len(lista) == 0:
    print('A sua espressão é valida!')
else:
    print('Sua espressão não é valida!')
