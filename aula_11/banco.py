idade = int (input("Informe a sua idade"))
salario = int (input("Informe o seu salário"))
tempo_trabalho = int (input("Informe o seu tempo de trabalho"))


print(f"Sua idade é {idade}, seu salário é {salario}, e o seu tempo de trabalho é {tempo_trabalho}")


if salario >= 2000 and idade >= 18 and tempo_trabalho >= 2:
    print("Seu pedido para um empréstimo foi realizado com sucesso.")

elif salario >= 5000 and idade >= 18:
    print("Seu empréstimo foi autorizado automaticamente.")

else:
    print("Seu pedido para um empréstimo foi negado.")


