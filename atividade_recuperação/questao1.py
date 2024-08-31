# Função para calcular o montante acumulado usando juros compostos
def calcular_montante(C, i, t):
    M = C * (1 + i) ** t
    return M


# Solicita ao usuário que insira os valores
while True:
    try:
        C = float(input("Digite o capital inicial aplicado (C): "))
        i = float(input("Digite a taxa de juros mensal (i) em decimal (ex: 0.05 para 5%): "))
        t = int(input("Digite o tempo (em meses) que o investimento será aplicado (t): "))

        # Verifica se os valores não são negativos
        if C < 0 or i < 0 or t < 0:
            print("Os valores não podem ser negativos. Por favor, insira valores válidos.")
        else:
            break
    except ValueError:
        print("Por favor, insira um valor numérico válido.")

# Calcula o montante acumulado
montante = calcular_montante(C, i, t)

# Mostra o resultado
print(f"O montante acumulado após {t} meses será: R$ {montante:.2f}")
