from funcoes import *

cartela = {
    'regra_simples': {1:-1,2:-1,3:-1,4:-1,5:-1,6:-1},
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

    while not jogada_feita:

        print("Dados rolados:", dados)
        print("Dados guardados:", dados_guardados)
        print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
        opcao = input()

        if opcao == '1':
            print("Digite o índice do dado a ser guardado (0 a 4):")
            i = int(input())
            dados, dados_guardados = guardar_dado(dados, dados_guardados, i)

        elif opcao == '2':
            print("Digite o índice do dado a ser removido (0 a 4):")
            i = int(input())
            dados, dados_guardados = remover_dado(dados, dados_guardados, i)

        elif opcao == '3':
            if rerrolagens < 2:
                dados = rolar_dados(5 - len(dados_guardados))
                rerrolagens += 1
            else:
                print("Você já usou todas as rerrolagens.")

        elif opcao == '4':
            imprime_cartela(cartela)

        elif opcao == '0':
            while True:
                print("Digite a combinação desejada:")
                cat = input()

                if cat in cartela['regra_avancada']:
                    if cartela['regra_avancada'][cat] != -1:
                        print("Essa combinação já foi utilizada.")
                    else:
                        cartela = faz_jogada(dados + dados_guardados, cat, cartela)
                        jogada_feita = True
                        break

                elif cat in ['1','2','3','4','5','6']:
                    num = int(cat)
                    if cartela['regra_simples'][num] != -1:
                        print("Essa combinação já foi utilizada.")
                    else:
                        cartela = faz_jogada(dados + dados_guardados, cat, cartela)
                        jogada_feita = True
                        break
                else:
                    print("Combinação inválida. Tente novamente.")

        else:
            print("Opção inválida. Tente novamente.")

    rodada += 1

imprime_cartela(cartela)

total = 0
simples = 0

for i in cartela['regra_simples']:
    if cartela['regra_simples'][i] != -1:
        total += cartela['regra_simples'][i]
        simples += cartela['regra_simples'][i]

for i in cartela['regra_avancada']:
    if cartela['regra_avancada'][i] != -1:
        total += cartela['regra_avancada'][i]

if simples >= 63:
    total += 35

print("Pontuação total:", total)
