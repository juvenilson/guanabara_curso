print('hello')
l1 = int(input('Digite o primeiro lado! '))
l2 = int(input('Digite o segundo lado! '))
l3 = int(input('Digite o terceiro lado!  '))

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('Isto éum triângulo!!')
    if l1 == l2 == l3:
        print('Este triângulo é um equilátero! ')
    elif l1 == l2 or l1 == l3 or l2 == l3:
        print('Este trinâgulo é um triângulo Isoceles. ')
    else:
        print('Este triângulo é um triângulo escaleno! ')
else:
    print('Estes lados não podem formar um triângulo!')
