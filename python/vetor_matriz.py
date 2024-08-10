# Solicita o número de linhas e colunas da matriz
linhas = int(input("Digite o número de linhas da matriz: "))
colunas = int(input("Digite o número de colunas da matriz: "))

# Inicializa a matriz
matriz = []

# Preenche a matriz com os elementos fornecidos pelo usuário
for i in range(linhas):
    linha = []
    for j in range(colunas):
        elemento = float(input(f"Digite o valor para a posição ({i + 1}, {j + 1}): "))
        linha.append(elemento)
    matriz.append(linha)

# Achando o maior, menor e a média dos elementos
todos_elementos = [elemento for linha in matriz for elemento in linha]
maior = max(todos_elementos)
menor = min(todos_elementos)
media = sum(todos_elementos) / len(todos_elementos)

# Exibe os resultados
print(f"Maior valor: {maior}")
print(f"Menor valor: {menor}")
print(f"Média dos valores: {media:.2f}")
