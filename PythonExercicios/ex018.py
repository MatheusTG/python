from math import sin, cos, tan, radians
n1 = float(input('Digite um ângulo: '))
print('O ângulode {} tem o Seno {:.2f}!'.format(n1, sin(radians(n1))))
print('O ângulo de {} tem o Cosseno {:.2f}'.format(n1, cos(radians(n1))))
print('O ângulo de {} tem o Tangente {:.2f}'.format(n1, tan(radians(n1))))
