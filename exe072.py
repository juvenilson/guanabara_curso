tupla = "zero", "um" ,"dois" ,"três" ,"quatro", "cinco", "seis", "sete", "oito", "nove", "dez"
position = 0
try:
    while 0 <= position <= 10:
        position = int(input("digite um número entre 0 e 10! "))
        print(f"Você digitou onúmero {tupla[position]}")
except:
    print("Este número não está na tupla!!")