def analisar_temperaturas(leituras: list[float]) -> tuple[float, int]:

    if not leituras:
        return 0.0, 0

    soma_temperaturas = 0.0
    alerta_calor = 0

    for temp in leituras:
        soma_temperaturas += temp
        if temp > 30.0:
            alerta_calor += 1

    media = soma_temperaturas / len(leituras)
    return media, alerta_calor


def main():
    temperaturas_dia = [22.5, 25.0, 31.2, 28.4, 19.8, 32.5, 30.1]

    # Desempacotando a tupla retornada pela função
    media, contagem_alertas = analisar_temperaturas(temperaturas_dia)

    print("--- Relatório Diário de Temperaturas ---")
    print(f"Temperatura média: {media:.2f} °C")
    print(f"Alertas de calor (> 30.0 °C): {contagem_alertas} ocorrência(s)")


if __name__ == "__main__":
    main()