anos = int(input('Quanto tempo na empresa? '))
salario = int(input('Qual o seu salario? '))
if anos <= 1: # se vc trabalhou menos de 1 ano ou um ano
    print('Você tem um aumento de 0%')
else:
    if anos >= 1 and anos < 10:
        salario_porcetagem = salario * (10/100) #
        print('O aumento de 10% é R$', salario_porcetagem + salario)

    else:
        salario_porcetagem = salario * (25/100)
        print('O aumento de 25% é R$', salario_porcetagem + salario)


