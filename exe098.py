def contador(i, f, p):
    if i < f:
        cont = i
        while cont <= f:
            print (cont, end=" ")
            cont += p
        print("Fim!")
    if i > f:
        cont = i
        while cont >= f:
            print(cont, end=" ")
            cont -= p
        print("Fim!")

contador(0, 10, 1)
contador(10, 0, 2)

print("Sua vez de criar uma contagem!")    
inicio = int(input("Inicio "))
passo = int(input("Passo "))
fim = int(input("Fim "))
contador(inicio, fim, passo)


