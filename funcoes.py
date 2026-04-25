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

def calcula_pontos_regra_simples(lista_faces):
    pontos = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
    for elemento in lista_faces:
        if elemento==1:
            pontos[1] += 1
        elif elemento==2:
            pontos[2] += 2
        elif elemento==3:
            pontos[3] += 3
        elif elemento==4:
            pontos[4] += 4
        elif elemento==5:
            pontos[5] += 5
        elif elemento==6:
            pontos[6] += 6
    return pontos

def calcula_pontos_soma(lista_faces):
    pontos = 0
    for elemento in lista_faces:
        pontos += elemento
    return pontos

def calcula_pontos_sequencia_baixa(lista_faces):
    pontos = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
    for elemento in lista_faces:
        if elemento==1:
            pontos[1] += 1
        elif elemento==2:
            pontos[2] += 1
        elif elemento==3:
            pontos[3] += 1
        elif elemento==4:
            pontos[4] += 1
        elif elemento==5:
            pontos[5] += 1
        elif elemento==6:
            pontos[6] += 1
    if pontos[1] >= 1 and pontos[2] >= 1 and pontos[3] >= 1 and pontos[4] >= 1:
        return 15
    elif pontos[2] >= 1 and pontos[3] >= 1 and pontos[4] >= 1 and pontos[5] >= 1:
        return 15
    elif pontos[3] >= 1 and pontos[4] >= 1 and pontos[5] >= 1 and pontos[6] >= 1:
        return 15
        
    
        