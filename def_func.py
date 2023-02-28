import emoji

#print(emoji.emojize("papel:page_facing_up:"))
#print(emoji.emojize(":right-facing_fist:"))
#print(emoji.emojize(":hand_with_fingers_splayed:"))
#print(emoji.emojize(":vulcan_salute:"))
#testando o commit
rock = ":right-facing_fist:"
paper = ":hand_with_fingers_splayed:"
scissor = ":vulcan_salute:"

#print(emoji.emojize(rock))
player = input("joquempo? ")
def emoji_by_player(player):
    if player == "rock":
        return(emoji.emojize(rock))
    elif player == "paper":
        return(emoji.emojize(paper))
    elif player == "scissor":
        return(emoji.emojize(scissor))

print(emoji_by_player(player))

