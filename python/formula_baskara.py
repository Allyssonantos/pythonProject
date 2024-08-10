import math

a = float(input('Digite o valor de a: '))
b = float(input('Digite o valor de b: '))
c = float(input('Digite o valor de c:'))

delta = b ** 2 - 4 * a + c

if a == 0 or delta < 0:
    print('não existe raiz real da equação.')
else:
    if delta == 0:
        x = -b / 2 * a
        print(f'A raiz quadrada de {x}')
    else:
        x1 = (-b + delta**(0.5))/(2*a)
        x2 = (-b - delta**(0.5))/(2*a)
        print('As raizes das equação são: x1 é', x1, 'x2 é', x2)












