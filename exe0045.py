from random import randint, choice
import time

"""Pedra/papel/tesoura"""

def imprime_que_perdeu(escolha_do_pc):
    print("Você perdeu! Eu escolhi {}".format(escolha_do_pc))

def imprime_que_ganhou(escolha_do_pc):
    print("Parabens você ganhou!! eu tinha escolhido {}".format(escolha_do_pc))

possibilidades_de_jogada = ["pedra", "papel", "tesoura"]
escolha_do_pc = choice(possibilidades_de_jogada)
print(escolha_do_pc)
escolha_do_gamer = str(input("Pedra, Papel ou Tesoura? ")).lower().strip("")
print("...Joquempô... ")
time.sleep(1)



matcher_dict = {
    ("pedra", "tesoura"): imprime_que_perdeu,
    ("papel", "pedra"): imprime_que_perdeu,
    ("tesoura", "papel"): imprime_que_perdeu,
    ("papel", "tesoura"): imprime_que_ganhou,
    ("tesoura", "pedra"): imprime_que_ganhou,
    ("pedra", "papel"): imprime_que_ganhou,
}

try:
    matcher_dict[(escolha_do_gamer, escolha_do_pc)](escolha_do_pc)
except KeyError:
    print(f"WOOOW nós empatamos, pois eu escolhi {escolha_do_pc} e você também!!")



# match (escolha_do_gamer, escolha_do_pc):
#     case ["pedra", "tesoura"]:
#         imprime_que_perdeu(escolha_do_pc)
#     case ["papel", "pedra"]:
#         imprime_que_perdeu(escolha_do_pc)
#     case ["tesoura", "papel"]:
#         imprime_que_perdeu(escolha_do_pc)
#     case ["pedra", "papel"]:
#         imprime_que_ganhou(escolha_do_pc)
#     case ["papel", "tesoura"]:
#         imprime_que_ganhou(escolha_do_pc)
#     case ["tesoura", "pedra"]:
#         imprime_que_ganhou(escolha_do_pc)
#     case ["papel", "papel"] | ["tesoura", "tesoura"] | ["pedra", "pedra"]:
#         print(f"WOOOW nós empatamos, pois eu escolhi {escolha_do_pc} e você também!!")
