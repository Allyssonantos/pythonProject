tam = int(input('Digite o tamanho do vetor: '))
v1 = [None]*tam

for i in range(len(v1)):
    if (i % 2) == 0:
        v1[i] = int(input(f'Digite o valor da posição {i}: '))
        while (v1[i] % 2) !=0:
            print('O numero não é par')
            v1[i] = int(input(f'Digite o valor da posção {i}: '))
    elif (i % 2) == 1:
        v1[i] = int(input(f'Digite o valor da posição {i}: '))
        while (v1[i] % 2) == 0:
            print('O numero não é impar')
            v1[i] = int(input(f'Digite o valor da posição {i}: '))
print(v1)