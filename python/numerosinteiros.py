import sys
maior = sys.maxsize
posmax = 0
n = int(input("Digite um valor: "))
for i in range(10):
     if n > maior:
         maior = n
         posmax = i
    n = int(input('Digite um valor: '))
print(f'Maior valor digitado: {maior}')
print(f'Posição do maior numero: ')

