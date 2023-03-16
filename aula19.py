"""dados = {
    "nome":"João",
    "idade": 24,
    "genero":"M"
}
print(dados["idade"])
print(dados.values())
print(dados.keys())
print(dados.items())
"""
estado = {}
brasil = []
qtd_de_estados = int(input("quantos estados voce quer registrar? "))
for i in range(0, qtd_de_estados):
    estado["nome"] = str(input("Nome do estado! ")).capitalize()
    estado["sigla"] = str(input("Sigla do estado! ")).upper()
    brasil.append(estado.copy())
for e in brasil:
    for v in e.values():
        print(v)