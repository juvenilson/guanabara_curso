"""Exercicio sobre modurlaridade"""
import moeda

preco = float(input("Digite um preço! "))
taxa = float(input("Digite uma taxa! "))

print(f"Com o almento de {taxa}% o valor vai ficar {moeda.aumentar(preco, taxa):.2f}")
print(f"com a redução de {taxa}% o valor vai ficar {moeda.diminuir(preco, taxa):.2f}")
print(f"o dobro do preço é {moeda.dobro(preco):.2f}")
print(f"A metade do preço é {moeda.metade(preco):.2f}")