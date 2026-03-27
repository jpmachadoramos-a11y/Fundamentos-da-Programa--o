# Variáveis da Pizzaria
FRETE = 2 #Constante Fake
pizza_sabor = input("informe o sabor da pizza - [fragon com requeijão], [calabresa], [mussarela], [banana com chocolate]")
pizza_tamanho = input("informe o tamanho da pizza - [pequena], [média], [grande]")
dia_semana = input("informe o dia da semana - [quarta], [quinta], [sexta], [sábado], [domingo]")

print(f"o sabor escolhido da pizza é {pizza_sabor}, o tamanho é {pizza_tamanho} e hoje é {dia_semana}")
# Promoções -> Estruturas condicionais

# Comprando qualquer pizza em qualquer tamanho no sábado, o refri é gratuito
if dia_semana == "sábado":
    print("pedido aceito com sucesso")
    print("o refri hoje é por conta da casa")
elif dia_semana == "domingo":
    print("pedido aceito com sucesso")
    print("o frete e o refri hoje é por conta da casa.")
elif pizza_sabor == "calabresa" and pizza_tamanho == "média":
    print("pedido aceito com sucesso")
    print("o frete hoje é por conta da casa.")

#comprando uma pizza de calabresa tamanho médio, o frete é gratuito

#Comprando qualquer pizza de qualquer tamanho no domingo, o frete e o refri são gratuitos