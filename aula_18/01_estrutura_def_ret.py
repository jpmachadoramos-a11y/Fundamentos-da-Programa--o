# Parêmetros Nomeados: Ao nomear os argumentos, a ordem não importa mais

def registrar_cliente (nome, telefone, endereco):
    print(f"=== DADOS DO CLIENTE ===")
    print(f"Cliente: {nome}")
    print(f"Telefone: {telefone}")
    print(f"Endereço: {endereco}")

# registrar_cliente(
#     telefone = "2194820442",
#     nome = "Ana Lima",
#     endereco = "Rua das Pizzas, 42"
# )

#---
# Retorno de Valores - Desempacotamento de retorno (unpacking): Retorna uma tupla com os valores
def resumo_pedido(itens, desconto=0):
    subtotal = sum(itens)
    valor_desconto = subtotal * desconto / 100
    total = subtotal - valor_desconto
    return subtotal, valor_desconto, total #devolve uma tupla (subtotal, valor desconto, total)

# Invocando e desempacotando a função/retorno
# print(resumo_pedido([35.0, 12.0, 8.5], desconto=10))
sub, desc, tot = resumo_pedido([35.0, 12.0, 8.5], desconto=10)
print(f"Subtotal: R$ {sub: .2f}")
print(f"Desconto: R$ {desc: .2f}")
print(f"Subtotal: R$ {tot: .2f}")