convite_restantes = 1000

while convite_restantes > 0:
    if convite_restantes >= 1:
        nome = str (input("Informe o seu nome: "))
        idade = int (input("Informe a sua idade: "))
        numero_convidados = int (input("Informe o número de convidados: "))
        convite_restantes -= numero_convidados
        print(f"Número de convites restantes: {convite_restantes}")


if idade >= 16 and convite_restantes >= 1:
    print("Entrada permitida.")

else:
    print("Entrada negada.")

while convite_restantes == 0:
    break



