import random
def rolar_dados(numero):
    lista = []
    for i in range(numero):
        lista.append(random.randint(1, 6))
    return lista

