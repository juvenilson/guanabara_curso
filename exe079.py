numeros = []
while True:
    r = str(input("quer adc um número?[S/N] ")).lower()[0].strip(" ")
    if r not in "s":
        print("responda apenas sim ou não")
    if r in "n":
        break
    n = int(input("digite um número! "))
    if n not in numeros:
        numeros.append(n)
        print("número adicionado")
    elif n in numeros:
        print("este número já existe na lista")
    
        
print("Aqui está sua lista; ", end="")
print(numeros)