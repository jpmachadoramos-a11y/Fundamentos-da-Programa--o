def calcular_media(nota1: float, nota2: float, nota3: float) -> float:
    """Calcula a média ponderada (pesos 2, 3, 5).
    Retorna -1.0 se alguma nota estiver fora do intervalo [0, 10].
    """
    for nota in [nota1, nota2, nota3]:
        if nota < 0 or nota > 10:
            return -1.0
    return round((nota1 * 2 + nota2 * 3 + nota3 * 5) / 10, 1)
print(calcular_media(7.0, 5.0, 8.0))