parimpar = [[], []]
for c in range(1, 8):
    v = int(input(f'Digite {c}° valor: '))

    if v % 2 == 0:
        parimpar[0].append(v)
    elif v % 2 == 1:
        parimpar[1].append(v)

parimpar[0].sort()
parimpar[1].sort()

print('=-=' * 12)
print(f'Os valores PARES digitados foram: {parimpar[0]}')
print(f'Os valores ÍMPARES digitados forma: {parimpar[1]}')
