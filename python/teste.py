def fibonacci(n):
    fib = [0, 1]  # Inicializa a lista com os dois primeiros números da sequência
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])  # Calcula o próximo número da sequência
    return fib

# Entrada de dados
n = int(input("Digite um numero: "))

# Calcula os N primeiros números de Fibonacci
sequencia = fibonacci(n)

# Saída
print(*sequencia)  # Imprime a sequência sem espaços extras entre os números