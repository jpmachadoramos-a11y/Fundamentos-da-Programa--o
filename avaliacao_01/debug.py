notas=[]
situação=[]

while True:
    print("""Menu Principal
          [1] Alunos cadastrados
          [2] Nome
          [3]nota01
          [4]nota02
          [5]nota03
          [6]consulta de situação
          [7] Sair
          """)
    opcao = input("Selecione uma opção: ")

    if opcao == "1":
        aluno_cadastro = float(input("Digite o número de alunos cadastrados: "))

    elif opcao == "2":
        nome_do_aluno = str(input("Digite o nome do aluno: "))
        continue
    elif opcao == "3":
      nota1 =float(input("digite tua nota01:"))
      notas.append(nota1)
      continue
    elif opcao == "4":
        nota2 = float(input("digite sau nota02:"))
        notas.append(nota2)
        continue
    elif opcao == "5":
        nota3 = float (input("digite sua nota03:"))
        notas.append(nota3) 
        continue
    elif opcao == "6":
      situação = sum (notas) / 3

    elif opcao == "7":
        print('Muito obrigado por utilizar o nosso sistema.')
        break

    print(f"aluno:{nome_do_aluno}")
    print (f"sua media é de {situação}") 
    if situação >= 7:
        print("Aluno aprovado.")

    elif situação >= 5:
        print("Aluno está de recuperação")

    else:
        print("Aluno está reprovado.")
    
    notas.append(situação)
    break
    
    
   