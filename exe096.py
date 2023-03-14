def area(lado1=0, lado2=0):
    calc_area = lado1 * lado2
    return(calc_area)
   

lado1 = float(input("Qual o primeiro lado? "))
lado2 = float(input("Qual o segundo lado? "))
print(F"A area tem {area(lado1, lado2):.2f} metros quadrados!")