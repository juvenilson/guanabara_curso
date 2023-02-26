"""Lendo daos de vários usuários!!!"""
pessoas_maior_id = 0
total_homens = 0
total_mulheres_menos20 = 0
idade = 0
sexo = " "
try:
    while True:
        idade = int(input("Qual a idade? "))
        sexo = str(input("Sexo? [M/F] ")).strip().upper()[0]
        while sexo not in "MF":
            sexo = str(input("Sexo? [M/F] ")).strip().upper()[0]
        if idade >= 18:
            pessoas_maior_id += 1
        if sexo == "M":
            total_homens += 1
        if sexo == "F" and idade <= 20:
            total_mulheres_menos20 += 1
        
        continua = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
        while continua not in "SN":
            continua = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
        if continua == "N":
            print("Encerrando...")
            break

    print(f"o Total de pessoas maiores de 18 foi {pessoas_maior_id}")
    print(f"O total de homens cadastrados foi {total_homens}")
    print(f"O total de mulheres mnores de 20 foi {total_mulheres_menos20}")
except:
    print("Dados invalidos!")