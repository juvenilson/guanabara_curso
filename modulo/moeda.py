def aumentar(preco, porcento):
    resp = preco + ((preco * porcento) / 100)
    return resp


def diminuir(preco, porcento):
    resp = preco - ((preco * porcento) / 100)
    return resp


def dobro(preco):
    resp = preco * 2
    return resp


def metade(preco):
    resp = preco / 2
    return resp
