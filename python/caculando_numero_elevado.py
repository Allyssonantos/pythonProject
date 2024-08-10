n = int(input("Digite um valor inteiro de 6 a 1999:  "))

while n < 6 or n > 1999:
    print('Valor inválido!')
    n = int(input('Digite um valor inteiro de 6 1999: '))

for i in range (1, n+1):
    if n % 2 == 0:
        print(f'{i}^2 = {i * i}')

