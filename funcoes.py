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
        return 
    else:
        return 0

def calcula_pontos_sequencia_alta(lista_faces):
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
    if pontos[1] >= 1 and pontos[2] >= 1 and pontos[3] >= 1 and pontos[4] >= 1 and pontos[5] >= 1:
        return 30
    elif pontos[2] >= 1 and pontos[3] >= 1 and pontos[4] >= 1 and pontos[5] >= 1 and pontos[6] >= 1:
        return 30
    else:
        return 0
def calcula_pontos_full_house(lista_faces):
    pontos = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
    soma = 0
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
    if (pontos[1] == 3 and pontos[2] == 2) or (pontos[1] == 2 and pontos[2] == 3):
        soma = pontos[1] + pontos[2]*2
        return soma
    elif (pontos[1] == 3 and pontos[3] == 2) or (pontos[1] == 2 and pontos[3] == 3):
        soma = pontos[1] + pontos[3]*3
        return soma
    elif (pontos[1] == 3 and pontos[4] == 2) or (pontos[1] == 2 and pontos[4] == 3):
        soma = pontos[1] + pontos[4]*4
        return soma
    elif (pontos[1] == 3 and pontos[5] == 2) or (pontos[1] == 2 and pontos[5] == 3):
        soma = pontos[1] + pontos[5]*5
        return soma
    elif (pontos[1] == 3 and pontos[6] == 2) or (pontos[1] == 2 and pontos[6] == 3):
        soma = pontos[1] + pontos[6]*6
        return soma
    elif (pontos[2] == 3 and pontos[3] == 2) or (pontos[2] == 2 and pontos[3] == 3):
        soma = pontos[2]*2 + pontos[3]*3
        return soma
    elif (pontos[2] == 3 and pontos[4] == 2) or (pontos[2] == 2 and pontos[4] == 3):
        soma = pontos[2]*2 + pontos[4]*4
        return soma
    elif (pontos[2] == 3 and pontos[5] == 2) or (pontos[2] == 2 and pontos[5] == 3):
        soma = pontos[2]*2 + pontos[5]*5
        return soma
    elif (pontos[2] == 3 and pontos[6] == 2) or (pontos[2] == 2 and pontos[6] == 3):
        soma = pontos[2]*2 + pontos[6]*6
        return soma
    elif (pontos[3] == 3 and pontos[4] == 2) or (pontos[3] == 2 and pontos[4] == 3):
        soma = pontos[3]*3 + pontos[4]*4
        return soma
    elif (pontos[3] == 3 and pontos[5] == 2) or (pontos[3] == 2 and pontos[5] == 3):
        soma = pontos[3]*3 + pontos[5]*5
        return soma
    elif (pontos[3] == 3 and pontos[6] == 2) or (pontos[3] == 2 and pontos[6] == 3):
        soma = pontos[3]*3 + pontos[6]*6
        return soma
    elif (pontos[4] == 3 and pontos[5] == 2) or (pontos[4] == 2 and pontos[5] == 3):
        soma = pontos[4]*4 + pontos[5]*5
        return soma
    elif (pontos[4] == 3 and pontos[6] == 2) or (pontos[4] == 2 and pontos[6] == 3):
        soma = pontos[4]*4 + pontos[6]*6
        return soma
    elif (pontos[5] == 3 and pontos[6] == 2) or (pontos[5] == 2 and pontos[6] == 3):
        soma = pontos[5]*5 + pontos[6]*6
        return soma
    else:
        return 0
    
def calcula_pontos_quadra(lista_faces):
    pontos = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
    soma = 0
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
    if pontos[1] == 4:
        for chave, numero in pontos.items():
            if numero < 4 and numero > 0:
                soma += chave*numero
            return pontos[1] + soma
    elif pontos[2] == 4:
        for chave, numero in pontos.items():
            if numero < 4 and numero > 0:
                soma += chave*numero
        return pontos[2]*2 + soma
    elif pontos[3] == 4:
        for chave, numero in pontos.items():
            if numero < 4 and numero > 0:
                soma += chave*numero
        return pontos[3]*3 + soma
    elif pontos[4] == 4:
        for chave, numero in pontos.items():
            if numero < 4 and numero > 0:
                soma += chave*numero
        return pontos[4]*4 + soma
    elif pontos[5] == 4:
        for chave, numero in pontos.items():
            if numero < 4 and numero > 0:
                soma += chave*numero
        return pontos[5]*5 + soma
    elif pontos[6] == 4:
        for chave, numero in pontos.items():
            if numero < 4 and numero > 0:
                soma += chave* numero
        return pontos[6]*6 + soma
    else:
        return 0
print(calcula_pontos_quadra([3, 2, 4, 4, 4, 2, 5, 4, 3, 3, 2, 1])) 
    
        