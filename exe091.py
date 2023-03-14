from random import randint
from operator import itemgetter

podio = dict()
dados = {
    "jogador1": randint(1, 6),
    "jogador2": randint(1, 6),
    "jogador3": randint(1, 6),
    "jogador4": randint(1, 6),
    }
for k, v in dados.items():
    print(f"O {k} lançou o dado e caiu o número {v}")
print("\nO pódio ficou com essa disposição!\n")
podio = sorted(dados.items(), key=itemgetter(1), reverse=True)
"""Comando para reorganizar os dados do maior para o menor"""
for p, t in enumerate(podio):
    print(f"{p + 1} lugar o {t[0]} com {t[1]} pontos.")