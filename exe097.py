texto = str(input("digite aqui sua mensagem! "))

def mensagem(txt):
    print("\n", "~" * len(txt), "\n")
    print(txt)
    print("\n", "~" * len(txt), "\n")

mensagem(texto)