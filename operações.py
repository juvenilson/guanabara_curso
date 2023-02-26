num1 = int(input("digite o primeiro número! "))
num2 = int(input("digite o sgundo número! " ))
operacao = int(input("""(1)somar.
(2)multiplicar
(3)maior
(4)novos números
(5)sair doprograma \n"""))
lista = []

while operacao != 5:
    if operacao == 1:
        print(num1 + num2)
    elif operacao == 2:
        print(num1 * num2)
    elif operacao == 3:
        lista.append(num1)
        lista.append(num2)
        print(max(lista))
        
    
    num1 = int(input("Digite um novo número! "))
    num2 = int(input("Digite um novo número! "))
    operacao = int(input("escolha outra operação "))
        
    
