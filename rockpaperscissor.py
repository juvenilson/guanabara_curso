import emoji 
from random import choice
from time import sleep
"""Importação de biblotecas para melhorar a apresentação do jogo."""
try:
    def show_who_win(choice_by_pc):
        """Função para retornar o resultado do jogo"""
        print(f"You win!!! i chose {choices_to_emoji(choice_by_pc)}, and you {choices_to_emoji(player_choice)}.")
    def show_who_lose(choice_by_pc):
        """Função para retornar o resultado do jogo"""
        print(f"You lose!! i chose {choices_to_emoji(choice_by_pc)}, and you {choices_to_emoji(player_choice)}.")
    def choices_to_emoji(choice):
        "Função para selecionar o emoji a ser apresentado em tela como resultado das escohas."
        match(choice):
            case "rock":
                return emoji.emojize(":right-facing_fist:")
            case "paper":
                return emoji.emojize(":hand_with_fingers_splayed:")
            case "scissor":
                return emoji.emojize( ":vulcan_salute:")
    possibilities_to_choose = ["rock", "paper", "scissor"]

    choice_by_pc = ""
    player_choice = ""
    player_choice = ""

    while player_choice != "end":
        """Loop para manter o jogo ativo enquanto for de vontade do jogador."""
        choice_by_pc = choice(possibilities_to_choose)
        print(choice_by_pc)
        player_choice = str(input("pick one! rock, paper or scissor ")).lower().strip("")
        print("="*20 + "Joquempo" + "="*20)
        sleep(1)
        """Funçaõ match para trabalhar com as possibiliades de resultados existentes para as ecolhas
        do jogador e também da máquina.
        """
        match(choice_by_pc, player_choice):
            case["rock", "scissor"]:
                show_who_lose(choice_by_pc)        
            case["paper", "rock"]:
                show_who_lose(choice_by_pc)
            case["scissor", "paper"]:
                show_who_lose(choice_by_pc)
            case["rock", "paper"]:
                show_who_win(choice_by_pc)
            case["paper", "scissor"]:
                show_who_win(choice_by_pc)
            case["scissor", "rock"]:
                show_who_win(choice_by_pc)
            case[_, _]:
                print(f"We have a draw!!! I chose {choices_to_emoji(choice_by_pc)}, and you too!")
except:
    print("Algo deu erado!!!")