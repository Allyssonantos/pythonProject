# ate 10 numeros
x = []
for i in range(10):
    numero = int(input(f"Digite o número {i + 1}: "))
    x.append(numero)

#Substituindo valores nulos e negativos por 1
for i in range(len(x)):
    if x[i] <= 0:
        x[i] = 1

# Exibindo o vetor após substituição
print("Vetor após substituição de valores nulos e negativos por 1:")
print(x)

#  Encontrando o maior valor do vetor e dobrando-o
maior_valor = max(x)  # Encontra o maior valor no vetor
indice_maior_valor = x.index(maior_valor)  # Encontra o índice do maior valor
x[indice_maior_valor] *= 2  # Dobra o valor do maior número

# Exibindo o vetor após dobrar o maior valor
print("Vetor após dobrar o maior valor:")
print(x)

# Mostrando todas as posições dos elementos cujo valor for maior que 10
print("Posições dos elementos cujo valor é maior que 10:")
for i in range(len(x)):
    if x[i] > 10:
        print(f"Posição {i}: {x[i]}")