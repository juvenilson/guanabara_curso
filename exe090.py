"""situação do aluno"""
aluno = {}
aluno["nome"] = str(input("Nome do aluno? ")).capitalize()
aluno["media"] = float(input(f"Média do(a) {aluno['nome']}? "))
if aluno["media"] < 7:
    aluno["situacao"] = "reprovado"
if 7 <= aluno["media"] <=10:
    aluno["situacao"] = "Aprovado"
print(f"O aluno {aluno['nome']} está na situação[ {aluno['situacao']}]")