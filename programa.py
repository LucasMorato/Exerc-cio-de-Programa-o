from funcoes import *

cartela = {
    'regra_simples': {
        1: -1, 2: -1, 3: -1,
        4: -1, 5: -1, 6: -1
    },
    'regra_avancada': {
        'sem_combinacao': -1,
        'quadra': -1,
        'full_house': -1,
        'sequencia_baixa': -1,
        'sequencia_alta': -1,
        'cinco_iguais': -1
    }
}

imprime_cartela(cartela)

rodada = 0

while rodada < 12:
    dados = rolar_dados(5)
    dados_guardados = []
    rerrolagens = 0
    jogada_feita = False

    while jogada_feita == False:
        print("Dados rolados:", dados)
        print("Dados guardados:", dados_guardados)
        print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
        opcao = input()

        if opcao == '1':
            print("Digite o índice do dado a ser guardado (0 a 4):")
            indice = int(input())
            resultado = guardar_dado(dados, dados_guardados, indice)
            dados = resultado[0]
            dados_guardados = resultado[1]

        elif opcao == '2':
            print("Digite o índice do dado a ser removido (0 a 4):")
            indice = int(input())
            resultado = remover_dado(dados, dados_guardados, indice)
            dados = resultado[0]
            dados_guardados = resultado[1]

        elif opcao == '3':
            if rerrolagens < 2:
                dados = rolar_dados(len(dados))
                rerrolagens = rerrolagens + 1
            else:
                print("Você já usou todas as rerrolagens.")

        elif opcao == '4':
            imprime_cartela(cartela)

        elif opcao == '0':
            valido = False

            while valido == False:
                print("Digite a combinação desejada:")
                categoria = input()

                if categoria == 'sem_combinacao' or categoria == 'quadra' or categoria == 'full_house' or categoria == 'sequencia_baixa' or categoria == 'sequencia_alta' or categoria == 'cinco_iguais':

                    if cartela['regra_avancada'][categoria] != -1:
                        print("Essa combinação já foi utilizada.")
                    else:
                        cartela = faz_jogada(dados + dados_guardados, categoria, cartela)
                        valido = True
                        jogada_feita = True

                elif categoria == '1' or categoria == '2' or categoria == '3' or categoria == '4' or categoria == '5' or categoria == '6':

                    numero = int(categoria)

                    if cartela['regra_simples'][numero] != -1:
                        print("Essa combinação já foi utilizada.")
                    else:
                        cartela = faz_jogada(dados + dados_guardados, categoria, cartela)
                        valido = True
                        jogada_feita = True

                else:
                    print("Combinação inválida. Tente novamente.")

            continue

        else:
            print("Opção inválida. Tente novamente.")

    rodada = rodada + 1

imprime_cartela(cartela)

total = 0
soma_simples = 0

for i in cartela['regra_simples']:
    if cartela['regra_simples'][i] != -1:
        total = total + cartela['regra_simples'][i]
        soma_simples = soma_simples + cartela['regra_simples'][i]

for i in cartela['regra_avancada']:
    if cartela['regra_avancada'][i] != -1:
        total = total + cartela['regra_avancada'][i]

if soma_simples >= 63:
    total = total + 35

print("Pontuação total:", total)
