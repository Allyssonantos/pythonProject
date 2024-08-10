# Definindo o cardápio
print('0: hambuguer - R$ 17,99')
print('1: cheeseburguer - R$ 13,99')
print('2: hotdog - R$ - 6,99')

opcao = int(input("Digite a opção desejada: "))
while opcao >= 0 and opcao <= 2:
    if opcao == 0:
        qnt = int(input('Digite a quantidade de hambugueres: '))
        total = 17.99 * qnt
        print(f'Você pediu {qnt} hamburgures. O total é R$ {total}')

    elif opcao == 1:

        qnt = int(input('Digite a quantidade de cheeseburguer: '))
        total = 13.99 * qnt
        print(f'Você pediu {qnt} cheeseburguer. O total é R$ {total}')

    elif opcao == 2:
        qnt = int(input('Digite a quantidade de hotdog: '))
        total = 6.99 * qnt
        print(f'Você pediu {qnt} hotdog. O total é R$ {total}')

    else:
        print("opcão invalida")


