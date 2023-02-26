print('Vamos calcular seu indice de massa corporea? ')
peso = float(input('Qual é o seu peso em qulogramas? '))
altura = float(input('Qual à sua altura em metros? '))
if altura > 100:
    imc = peso / ((altura / 100) ** 2) 
    if imc < 18.5:
        print('Você está abaixo do peso ideal!')
    elif 18.5 < imc < 25:
        print('Você ésta coom o peso ideal para sua estatura!')
    elif 25 < imc < 30:
        print('Você ésta com sobrepeso! ')
    elif 30 < imc < 40:
        print('Você está em condiçâo de obesidade')
    elif 40 < imc:
        print('Você está em condição de obeidade mórbida')
else:
    imc = peso / (altura ** 2)
    if imc < 18.5:
        print('Você está abaixo do peso ideal!')
    elif 18.5 < imc < 25:
        print('Você ésta coom o peso ideal para sua estatura!')
    elif 25 < imc < 30:
        print('Você ésta com sobrepeso! ')
    elif 30 < imc < 40:
        print('Você está em condiçâo de obesidade')
    elif 40 < imc:
        print('Você está em condição de obeidade mórbida')


