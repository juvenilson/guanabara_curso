n = 0
cont = 0
soma = 0
while n != 999:
    n = int(input("Digite o número! "))
    if n == 999:
        break
    cont += 1
    soma += n
print(f"A soma dos números é {soma}, e o total de números foi {cont}")
