# Função para preencher o vetor x com 10 números inteiros
def preencher_vetor(tamanho):
    vetor = []
    for i in range(tamanho):
        valor = int(input(f"Digite o valor para a posição {i}: "))
        vetor.append(valor)
    return vetor

# Função para substituir valores não negativos por -1
def substituir_nao_negativos(vetor):
    for i in range(len(vetor)):
        if vetor[i] >= 0:
            vetor[i] = -1
    return vetor

# Função para somar +3 aos valores menores que 5
def somar_mais3_menores_que_5(vetor):
    for i in range(len(vetor)):
        if vetor[i] < 5:
            vetor[i] += 3
    return vetor

# Função para encontrar a posição e o valor do maior e menor elemento do vetor
def encontrar_maior_menor(vetor):
    maior_valor = max(vetor)
    menor_valor = min(vetor)
    posicao_maior = vetor.index(maior_valor)
    posicao_menor = vetor.index(menor_valor)
    return maior_valor, posicao_maior, menor_valor, posicao_menor

# Programa principal
def main():
    # Passo 1: Preencher o vetor com 10 números inteiros
    tamanho_vetor = 10
    vetor = preencher_vetor(tamanho_vetor)
    print(f"Vetor original: {vetor}")

    # Passo 2: Substituir todos os valores não negativos por -1
    vetor = substituir_nao_negativos(vetor)
    print(f"Vetor após substituir valores não negativos por -1: {vetor}")

    # Passo 3: Somar +3 aos valores menores que 5
    vetor = somar_mais3_menores_que_5(vetor)
    print(f"Vetor após somar +3 aos valores menores que 5: {vetor}")

    # Passo 4: Encontrar a posição e os valores do maior e menor elemento
    maior_valor, posicao_maior, menor_valor, posicao_menor = encontrar_maior_menor(vetor)
    print(f"Maior valor: {maior_valor}, Posição: {posicao_maior}")
    print(f"Menor valor: {menor_valor}, Posição: {posicao_menor}")

if __name__ == "__main__":
    main()
