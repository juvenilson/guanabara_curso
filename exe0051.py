'''showing an AP with two inputs'''
pn = int(input("digite o primeiro número! "))
r = int(input("digite o segundo número! "))

for c in range(pn, (pn * r * 10), r):
    print(c)
print("Dado os parametros inputados {} e {},".format(pn, r, ))
print("Teremos os seguintes números nessa progreção aritimetica!")
    