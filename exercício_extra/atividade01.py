#     Até 100 kWh → R$ 0,40 por kWh ->40
#     De 101 a 200 kWh → R$ 0,60 por kWh ->40 + 60 = 100 
#     Acima de 200 kWh → R$ 0,90 por kWh
#     Exibir ao final: o consumo informado, a faixa de tarifa aplicada e o valor total a pagar.
#     Caso o consumo informado seja negativo, exibir uma mensagem de valor inválido.

#Declaração das variáveis Globais - snake_case
valor_ate_100kwa = 0.40
valor_ate_200kwa = 0.60
valor_acima_200kwa = 0.90

print(f"------Seja bem vindo ao programa de calcúlo de energia elétrica------")
while True:
    input_kwa = input(f"Digite a quantidade de kwa consumidos ou sair para encerrar)")
    if input_kwa.lower() == "sair":
        print("Adeus. Encerrando o programa. Obrigado por utilizar!\n")
        break
    elif not input_kwa.isdigit():
        print("Entrada inválida! Por favor digite um número ou sair para encerrar.\n")
        continue
    else:
        kwh = int(input_kwa)
        if kwh <= 100:
            valor_total = kwh * valor_ate_100kwa
            print("A faixa de consumo é: 0 a 100kwh")
            print(f"O valor total da conta de energia é: R${valor_total}.2f")
        elif kwh <=200:
            valor_total = 100 * valor_ate_100kwa + (kwh - 100) * valor_ate_200kwa
            print("A faixa de consumo é entre: 100 a 200kwh")
            print(f"O valor total da conta de energia é: R${valor_total}.2f")
        else:
            valor_total = 100 * valor_ate_100kwa + 100 * valor_acima_200kwa + (kwh - 200) * valor_acima_200kwa
            print("A faixa de consumo é entre: 200kwh ou mais")
            print(f"O valor total da conta de energia é: R${valor_total}.2f")

              





