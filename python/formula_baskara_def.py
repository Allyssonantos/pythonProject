import math
def calcular_bhaskara(a, b, c):
    delta = b ** 2 - 4 * a * c
    print(f"Delta = {delta}")
    #caucular de á raizes
    if  delta < 0:
        return print('não existe raiz real da equação.')
    elif delta == 0:
        x = -b/(2*a)
        return x
    else:
        # Calcula as raízes
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        return x1,x2

#digitar os valores

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input(("Digite o valor de c: ")))

resposta = calcular_bhaskara(a, b, c)
print(resposta)


