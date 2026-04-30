quantidade_alunos =[]
media_turma = []
notas = []
while True:
    print("""Menu Principal
          [1] Alunos cadastrados
          [2] Nome
          [3] Primerio Semestre
          [4] Segundo Semestre
          [5] Terceiro Semestre
          [6] Sair
          """)
    opcao = input("Selecione uma opção: ")

    estado_aluno = sum(notas) / 3

    if opcao == "1":
        aluno_cadastro = float(input("Digite o número de alunos cadastrados: "))

    elif opcao == "2":
        str(input("Digite o nome do aluno: "))

    elif opcao == "3":
        nota01 = float(input("Digite a nota do aluno no Primeiro Semestre"))
        notas.append(nota01)

    elif opcao == "4":
        nota02 = float(input("Digite a nota do aluno no Segundo Semestre"))
        notas.append(nota02)

    elif opcao == "5":
        nota03 = float(input("Digite a nota do aluno no Terceiro Semestre"))
        notas.append(nota03)


    if estado_aluno >= 7:
        print("Aluno aprovado.")

    elif estado_aluno >= 5:
        print("Aluno está de recuperação")

    else:
        print("Aluno está reprovado.")

    media_turma.append(estado_aluno)

    






    






    
