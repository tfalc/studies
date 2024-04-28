def imprimir_rank_heroi(qtd_exp):
    ranks = {
        range(0, 1001): "Ferro",
        range(1001, 2001): "Bronze",
        range(2001, 5001): "Prata",
        range(5001, 7001): "Ouro",
        range(7001, 8001): "Platina",
        range(8001, 9001): "Ascendente",
        range(9001, 10001): "Imortal",
    }

    if qtd_exp > 10000:
        return "Radiante"

    for intervalo_exp, rank in ranks.items():
        if qtd_exp in intervalo_exp:
            return rank


def prompt_heroi_e_exp():
    nome = input("Digite o nome do heroi: ")
    etd_nivel = int(input("Digite o nivel do heroi: "))
    nivel = imprimir_rank_heroi(etd_nivel)

    resultado = f"O heroi de nome {nome} esta no nivel {nivel}.\n"
    print(resultado)


# TESTES
""" imprimir_rank_heroi(500)  # FERRO
imprimir_rank_heroi(1001)  # BRONZE
imprimir_rank_heroi(1500)  # BRONZE
imprimir_rank_heroi(2500)  # PRATA
imprimir_rank_heroi(5500)  # OURO
imprimir_rank_heroi(7500)  # PLATINA
imprimir_rank_heroi(8500)  # ASCENDENTE
imprimir_rank_heroi(9500)  # IMORTAL
imprimir_rank_heroi(19500)  # RADIANTE
imprimir_rank_heroi(39500)  # RADIANTE
imprimir_rank_heroi(10000)  # RADIANTE 
"""  # Final dos testes manuais

while True:
    prompt_heroi_e_exp()
