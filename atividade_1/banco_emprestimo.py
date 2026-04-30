print("Sistema de Empréstimo Bancário")

# Entradas de Dados
idade = int(input("Digite a idade: "))
salario = float(input("Digite o salário do cliente: "))
tempo_trabalhado = int(input("Digite o tempo de trabalho (em anos): "))

# Estrturas Condicionais
if idade < 18:
    print("Cliente menor de idade.")
elif salario >= 5000:
    print("Empréstimo aprovado automaticamente.")
elif idade >= 18 and salario >= 2000 and tempo_trabalhado >= 2:
    print("Empréstimo aprovado.")
else:
    print("Empréstimo negado.")
# Verificar a idade, o salario, e o tempo de trabalho
