from datetime import datetime
print("Vamos registrar uma pessoa!")
registro = dict()
registro["nome"] = str(input("Nome? ")).capitalize()
ano_nacimento = int(input("ano de nascimento? "))
registro["idade"] = datetime.now().year - ano_nacimento 
registro["ctps"] = int(input("Número da carteira de trabalho? [0 para inexitente]"))
if registro["ctps"] != 0:
    registro["ano_contratacao"] = int(input("Ano de contratação? "))
    registro["salario"] = float(input("Salario recebido? "))
    registro["aposenta"] = ((35 - (datetime.now().year - registro["ano_contratacao"])) + registro["idade"] )
if registro["ctps"] == 0:
    registro["ctps"] = "não tem"

for i, k in registro.items():
    print(i, k)