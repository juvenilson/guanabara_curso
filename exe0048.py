'''Números divisiveis por 3 entre 1 e 500'''
c = 0
for i in range(0, 500):
    if i % 3 == 0:
        c = c + i
print(c)

user = 0