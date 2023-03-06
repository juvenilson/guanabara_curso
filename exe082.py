pessoas = []
grupo = []
continuar_cadastro = True
maiores = []
while continuar_cadastro:
    try:
        r = str(input("Você quer cadastrar alguém?[S/N] ")).strip(" ").lower()[0]
        if r == "s":
            pessoas.append(str(input("Qual o primeiro nome? ")).capitalize())
            pessoas.append(int(input("Qual à idade? ")))
            grupo.append(pessoas[:])
            print("Pessoa cadastrada com sucesso!!")
            if pessoas[1] >= 18:
                maiores.append(pessoas[0])
            pessoas.clear()
        elif r == "n":
            print("Então, até logo!")
            continuar_cadastro = False
            print(len(maiores) + "pessoas maiores de idade")
            for n, i in grupo:
                print(f"{n} foi registrado, e tem {i} anos de idade!")

        else:
            raise Exception("Você prresisa responder (S) para sim e (N) para não!")
    except Exception as erro:
        print(erro)
        continuar_cadastro = False

