frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
#inverso = junto[::-1] Outra maneira de fazer!
for c in range(len(junto)-1, -1, -1):
    inverso += junto[c]
if inverso == junto:
    print('Essa frase é um palindrolo, ou seja ela é igual de frente para traz!')
    print('Antes: {}\nDepois: {}'.format(junto, inverso))
else:
    print('Essa frase não é um palindromo!')
    print('Antes: {}\nDepois: {}'.format(junto, inverso))
