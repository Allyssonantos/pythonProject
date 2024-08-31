def obter_valor_inteiro(mensagem):
    """ Solicita um valor inteiro positivo ao usuário. """
    while True:
        try:
            valor = int(input(mensagem))
            if valor < 0:
                print("O valor deve ser maior ou igual a zero. Tente novamente.")
            else:
                return valor
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

def calcular_segundos(horas, minutos, segundos):
    """ Calcula o total de segundos desde o início do dia. """
    return horas * 3600 + minutos * 60 + segundos

def main():
    print("Por favor, insira as seguintes informações:")

    # Obter as horas, minutos e segundos do usuário
    horas = obter_valor_inteiro("Digite a hora (0-23): ")
    minutos = obter_valor_inteiro("Digite os minutos (0-59): ")
    segundos = obter_valor_inteiro("Digite os segundos (0-59): ")

    # Calcular o total de segundos
    total_segundos = calcular_segundos(horas, minutos, segundos)

    # Mostrar o resultado
    print(f"{horas} hora(s), {minutos} minuto(s) e {segundos} segundo(s) correspondem a {total_segundos} segundos desde o início do dia.")

if __name__ == "__main__":
    main()
