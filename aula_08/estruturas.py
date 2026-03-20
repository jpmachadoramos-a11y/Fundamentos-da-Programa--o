# Estrutura de repetição
#-if (se) -> verifica se uma condição é true (verdadeira) - Se for, ele executa o código
#-elif (senão se) -> é usado para testar várias condições. Ele só executa se todas as condições anteriores forem falsas
#-else (senão) -> executa o código se a condição if for false (falsa)

# idade_usuario = 15
# #-Se o usuario for maior de 18 anos, eu vou passar a informação: você é maior de idade, senão você é menor de idade
# if idade_usuario >= 18:
#     print("você é maior de idade") 
# else:
#     print("você é menor de idade")

idade = 73
if idade >= 18:
    print("você é maior de idade")
elif idade >=0 and idade >= 18:
    print("você é jovem de idade")
elif idade >= 70:
    print("você é experiente de idade")
else:
    print("você é menor de idade")