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
    
    print("Escolha o aluno pelo número do indice, para finalizar[999]")
    nota_dos_alunos = int(input("quer ver notas de qual aluno? "))
    while nota_dos_alunos != 999:
        if nota_dos_alunos == 999:
            print("Até mais!!!")
            break
        if nota_dos_alunos <= len(ficha):
            print(f"o aluno {ficha[nota_dos_alunos -1][0]} obteve as notas {ficha[nota_dos_alunos -1][1]}!")
            nota_dos_alunos = int(input("quer ver notas de qual aluno? "))


except Exception as error:
    print(f"O erro de '{error}' foi cometido durante o processo!")
    


   