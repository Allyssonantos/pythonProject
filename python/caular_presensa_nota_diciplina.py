presenca = int(input('Digite a % da sua presença: '))
nota_prova = float(input('Digite a sua nota na prova: '))
nota_atividade = float(input('Digite a sua sua nota na atividade: '))

media_final = nota_prova + nota_atividade / 2
recuperacao_paralela = media_final / 2
recuperacao_final = recuperacao_paralela + media_final / 2


if presenca >= 75 and media_final >= 6:
    print('Você está aprovado!')
else:
    print('Você não foi aprovado')
    if media_final <= 6:
        recuperacao_paralela = float(input('Digite a nota do recuperção paralela: '))
        if recuperacao_paralela >= 6:
            print('Você foi aprovado')
        else:
            print('Você tem que fazer a recuperação final!')
            recuperacao_final = float(input('Digite a nota da recuperação final: '))
            if recuperacao_final >= 6:
                print('Você foi aprovado')
            else:
                print('Você foi reprovado!')


