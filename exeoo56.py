'''escrever um programa que leia dados(idade, nome, e genero)
de seis individuos e mostre a media das idades, quem é o mais velho dos 
homens, e qual das mulheres ainda è menor de idade'''
grupo = []
idade = 0
mas = []
fem = []
count = 0
for i in range(0,2):
    id = int(input("qual sua idade? "))
    no = str(input("Qual seu nome?"  )).capitalize()
    ge = str(input("Qual seu genero? ")).lower()
    idade = idade + id
    grupo.append([id, no, ge])
    count +=1

    if ge == "mas":
        mas.append([id, no, ge])
       
    elif ge == "fem":
        fem.append([id, no, ge])
print(idade / count)


