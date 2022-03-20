def fatorial(n=0, show=False):
    """
    ==> Use para calcular o fatorial de um número!
    :param n: Escolha o número para calcular
    :param show: Mastra conta do fatorial(OPCIONAL)
        Ex: 5 x 4 x 3 x 2 x 1 = 120
    :return: O valor de um fatorial de valor n!
    """
    f = 1
    for c in range(n, 0, -1):
        f *= c
        if show:
            print(c, end='')
            if c != 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
    print(f)


fatorial(5, True)
