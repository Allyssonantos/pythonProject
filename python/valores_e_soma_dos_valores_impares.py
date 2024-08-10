x = int(input('Digite o valor do n1: '))
y = int(input('Digite o valor do n2: '))
soma = 0
if = x < y:
    inicio = x + 1
    while inicio < y:
        if inicio % 2 == 1:
            soma = soma + inicio
        inicio = inicio + 1
    print(f'A soma dos números impares entre {x} e {y} é {soma}')
else:
    inicio = y + 1
    while inicio < x:
        if inicio % 2 == 1:
            soma = soma + inicio
        inicio = inicio + 1
    print()


