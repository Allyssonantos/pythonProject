idade = int(input("Quantos anos você tem? "))

if idade < 18:
    print("Você é menor de 18 anos, não pode tirar a CNH.")
else:
    print("Você tem 18 anos ou mais, pode tirar a CNH.")

    prova_teoria = input("Você foi aprovado na prova teórica? (sim/não) ")
    if prova_teoria == "sim":

        prova_pratica = input("Você foi aprovado na prova prática? (sim/não) ")
        if prova_pratica == "sim":
            print(" Voce pode tirar a CNH.")
        else:
            print("Você foi reprovado na prova prática, não pode tirar a CNH.")

    else:
        print("Você foi reprovado na prova teórica, não pode tirar a CNH.")
