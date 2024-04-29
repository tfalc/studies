def calcular_nivel_rankeado(vitorias, derrotas):
    """
    Calcula o nível rankeado do jogador com base em suas vitórias e derrotas.

    Args:
      vitorias: Número de vitórias do jogador.
      derrotas: Número de derrotas do jogador.

    Returns:
      Uma string com a mensagem informando o saldo de vitórias e o nível rankeado.
    """

    saldo_vitorias = vitorias - derrotas

    if saldo_vitorias < 10:
        nivel = "Ferro"
    elif 10 <= saldo_vitorias < 21:
        nivel = "Bronze"
    elif 21 <= saldo_vitorias < 51:
        nivel = "Prata"
    elif 51 <= saldo_vitorias < 81:
        nivel = "Ouro"
    elif 81 <= saldo_vitorias < 91:
        nivel = "Diamante"
    elif 91 <= saldo_vitorias <= 100:
        nivel = "Lendário"
    else:
        nivel = "Imortal"

    mensagem = f"O Herói tem um saldo de {saldo_vitorias} vitórias e está no nível {nivel}."
    return mensagem


# Exemplo de uso
vitorias_jogador = int(input("Digite o número de vitórias do jogador: "))
derrotas_jogador = int(input("Digite o número de derrotas do jogador: "))

nivel_rankeado = calcular_nivel_rankeado(vitorias_jogador, derrotas_jogador)
print(nivel_rankeado)