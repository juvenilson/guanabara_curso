ficha = []
resposta = "s"
try:
    while resposta != "n":
        resposta = str(input("Quer cadastrar um aluno?[S/N] ")).lower()[0].strip("")

        if resposta == "s":
            aluno = str(input("Nome do aluno? ")).strip(" ").capitalize()
            nota1 = float(input("Qual a primeira nota? "))
            nota2 = float(input("Qual a segunda nota? "))
            media = (nota1 + nota2) / 2
            ficha.append([aluno, [nota1, nota2], media])
    print(f"{'indice':<10}{'Nome':<10}{'Média':>10}")
    for i, a in enumerate(ficha):
        print(f"{i + 1:<10}{a[0]:<10}{a[2]:>10}") 
        """Esse for foi criado para classificar a lista"""      



except:
    pass


   