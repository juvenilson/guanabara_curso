from time import sleep

contagem = 10
for c in range(11, 0, -1):
    print(contagem)
    sleep(1)
    contagem = contagem -1
print("Fogo!!")