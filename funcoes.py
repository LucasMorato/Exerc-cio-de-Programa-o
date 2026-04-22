import random
def rolar_dados(numero):
    lista = []
    for i in range(numero):
        lista.append(random.randint(1, 6))
    return lista

def guardar_dado(dados_rolados, dados_no_estoque, dado_para_guardar):
    resultado = []
    teste = []
    novo_dado = dados_rolados[dado_para_guardar]
    dados_no_estoque.append(novo_dado)
    for i in range(len(dados_rolados)):
        if i != dado_para_guardar:
            teste.append(dados_rolados[i])
    resultado.append(teste)
    resultado.append(dados_no_estoque)
    return resultado

def remover_dado(dados_rolados, dados_no_estoque, dado_para_remover):
    resultado = []
    teste = []
    for i in range(len(dados_no_estoque)):
        if i != dado_para_remover:
            teste.append(dados_no_estoque[i])
    dados_rolados.append(dados_no_estoque[dado_para_remover])
    resultado.append(dados_rolados)
    resultado.append(teste)
    return resultado

