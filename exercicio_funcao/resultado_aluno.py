def verificar_situacao(media: float, verificar_honra: bool = True) -> tuple:
    """Retorna (situacao, mensagem_honra) com base na média."""
    if media >= 7.0:
        situacao = "Aprovado"
    elif media >= 5.0:
        situacao = "Recuperação"
    else:
        situacao = "Reprovado"

    honra = "Menção Honrosa" if (verificar_honra and media >= 9.0) else ""
    return situacao, honra
print(verificar_situacao(3.0))