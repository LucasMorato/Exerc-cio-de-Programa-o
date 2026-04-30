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
    guardados = []
    rerrolagens = 0
    terminou = False

    while not terminou:

        print("Dados rolados:", dados)
        print("Dados guardados:", guardados)
        print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
        op = input()

        if op == '1':
            print("Digite o índice do dado a ser guardado (0 a 4):")
            i = int(input())
            dados, guardados = guardar_dado(dados, guardados, i)

        elif op == '2':
            print("Digite o índice do dado a ser removido (0 a 4):")
            i = int(input())
            dados, guardados = remover_dado(dados, guardados, i)

        elif op == '3':
            if rerrolagens < 2:
                dados = rolar_dados(5 - len(guardados))
                rerrolagens += 1
            else:
                print("Você já usou todas as rerrolagens.")

        elif op == '4':
            imprime_cartela(cartela)

        elif op == '0':
            while True:
                print("Digite a combinação desejada:")
                c = input()

                if c in cartela['regra_avancada']:
                    if cartela['regra_avancada'][c] != -1:
                        print("Essa combinação já foi utilizada.")
                    else:
                        cartela = faz_jogada(dados + guardados, c, cartela)
                        terminou = True
                        break

                elif c in ['1','2','3','4','5','6']:
                    n = int(c)
                    if cartela['regra_simples'][n] != -1:
                        print("Essa combinação já foi utilizada.")
                    else:
                        cartela = faz_jogada(dados + guardados, c, cartela)
                        terminou = True
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
