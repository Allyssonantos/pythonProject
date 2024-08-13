soma_pares = 0
cont_pares = 0
maior_impar = None
total_numeros = 0

while True:
    numero = int(input("Digite um número inteiro : "))

    if numero == 0:
        break # enterronper o codigo

    # Contando o total de números digitados, sem os zeros
    total_numeros += 1

    # Verificando se o número é par ou ímpar
    if numero % 2 == 0:
        soma_pares += numero
        cont_pares += 1
    else:
        if maior_impar is None or numero > maior_impar:
            maior_impar = numero

# Cálculo e  print  dos resultados
if cont_pares > 0:
    media_pares = soma_pares / cont_pares
    print(f"Média dos números pares: {media_pares:.2f}")
else:
    print("Nenhum número par foi digitado")

if maior_impar is not None:
    print(f"Maior número ímpar: {maior_impar}")
else:
    print("Nenhum número ímpar foi digitado")

print(f"Total de números digitados: {total_numeros}")
