# PONTIFÍCIA UNIVERSIDADE CATÓLICA DO PARANÁ
# ESCOLA POLITÉCNICA
# ANÁLISE E DESENVOLVIMENTO DE SISTEMAS
# RACIOCÍNIO COMPUTACIONAL
# JAIRO MOISÉS STUEHLER BANKHARDT
# IMPLEMENTAÇÃO DO JOGO ZOMBIE DICE

import random

# INICIALIZAÇÃO DE VARIÁVEIS
TIROS_MATADORES = 3
CEREBROS_VITORIOSOS = 13

verde = "CPCTPC"      # C = Cérebro, P = Passos e T = Tiro
amarelo = "TPCTPC"
vermelho = "TPTCPT"
jogadores = []  # lista que irá conter o [nome dos jogadores, total de cérebros devorados]
turno = 0
qtd_jogadores = 0
total_cerebros = []  # Contador de cérebros degustados pelos jogadores
mais_um_jogador = "S"
fim_jogo = False

# INÍCIO DO JOGO
print("\n\n************\nZOMBIE DICE\n************\n")
print("Vamos começar.")

# JOGADORES - QUANTIDADE E NOMES
print("Primeiro vamos conhecer os jogadores.\n")
while mais_um_jogador == "S":
    total_cerebros.append(0)
    qtd_jogadores += 1
    nome_jogador = input("Qual o nome do Jogador número %d? " % qtd_jogadores)
    jogadores.append(nome_jogador)
    if qtd_jogadores >= 2:
        mais_um_jogador = input("Alguém mais vai jogar? (S/N) ").upper()
        while mais_um_jogador != 'S' and mais_um_jogador != 'N':
            print("Opção inválida. Digite S para Sim ou N para Não.")
            mais_um_jogador = input("Alguém mais vai jogar? (S/N) ").upper()

print("\nPRONTO. VAMOS COMEÇAR O JOGO.\n")

while not fim_jogo:
    turno += 1
    print("-----------------")
    print(f"TURNO NÚMERO {turno}")
    print("-----------------")
    print(jogadores)
    print(total_cerebros)
    print('')
    for cont_jog in range(qtd_jogadores):
        contC = 0
        contT = 0
        contP = 0
        tubo = "GGGGGGYYYYRRR"  # G = Verde, Y = Amarelo e R = Vermelho
        fim_turno = False
        dados_sorteados = ['', '', '']  # Guardará a cor e face dos dados sorteados

        print(f"~~~~~~ É a vez de {jogadores[cont_jog].upper()} ~~~~~~")
        print(f'Você está com {total_cerebros[cont_jog]}.\n')

        while not fim_turno:
            for i in range(3):

                # Sorteia dados do tubo se não haver passos sorteados na rodada anterior
                if dados_sorteados[i] == '':
                    indice_tubo = random.randrange(len(tubo))
                    dados_sorteados[i] = [tubo[indice_tubo], '']
                    tubo = tubo[0:indice_tubo] + tubo[indice_tubo + 1:len(tubo)]

                # Sorteia as faces
                if dados_sorteados[i][0] == "G":
                    cor = "verde"
                    dados_sorteados[i][1] = random.choice(verde)
                elif dados_sorteados[i][0] == "Y":
                    cor = "amarelo"
                    dados_sorteados[i][1] = random.choice(amarelo)
                else:
                    cor = "vermelho"
                    dados_sorteados[i][1] = random.choice(vermelho)

                # Incrementa contadores
                if dados_sorteados[i][1] == "C":
                    face = "cérebro"
                    contC += 1
                    dados_sorteados[i] = ''
                elif dados_sorteados[i][1] == "P":
                    face = "passo"
                    contP += 1
                else:
                    face = "tiro"
                    contT += 1
                    dados_sorteados[i] = ''

                print(f"*** O dado número {i+1} é de cor {cor.upper():^8} e caiu um {face.upper():^7}. ***")

            print("Cérebros: {} | Passos: {} | Tiros: {}".format(contC, contP, contT))
            print(f"Tubo: {tubo} [{len(tubo)}] > Dados elegíveis: {contP + len(tubo)}")
            print(f"Total de cérebros devorados: {total_cerebros[cont_jog]} --> {total_cerebros[cont_jog]+contC}")

            # VERIFICA SE É POSSÍVEL CONTINUAR O TURNO
            if contT >= TIROS_MATADORES:  # Levou tantos tiros ou mais do que o permitido para continuar
                print(f"Você recebeu muitos tiros [{contT}]. Seu turno acabou e você não somou cérebros.\n\n")
                fim_turno = True
            elif contP + len(tubo) < 3:  # Não há mais dados suficientes para jogar novamente
                print(f"Número de dados insuficientes para uma nova rodada. [{contP + len(tubo)}].")
                print("Cérebros contabilizados e turno finalizado.\n\n")
                total_cerebros[cont_jog] += contC
                fim_turno = True
            else:
                jogar_novamente = input("Você quer jogar novamente neste turno? (S/N) ").upper()
                while jogar_novamente != 'S' and jogar_novamente != 'N':
                    print("Opção inválida. Digite S para Sim ou N para Não.")
                    jogar_novamente = input("Você quer jogar novamente neste turno? (S/N) ").upper()
                if jogar_novamente == "N":  # Não deseja continuar a jogar neste turno
                    total_cerebros[cont_jog] += contC
                    print("\n")
                    fim_turno = True
                else:  # Quer continuar a lançar os dados neste turno
                    contP = 0
                    print("")

    # VERIFICA SE CHEGAMOS AO FIM DO JOGO E SE HOUVE EMPATE
    maior_cerebro = max(total_cerebros)
    if maior_cerebro >= CEREBROS_VITORIOSOS:
        vencedor = []
        for n in range(len(total_cerebros)):
            if total_cerebros[n] == maior_cerebro:
                vencedor.append(n)
        if len(vencedor) > 1:  # Houve empate e terá um novo turno de desempate
            print("-------------------------------")
            print("TEMOS UM EMPATE.")
            print(f"Cérebros degustados: {total_cerebros}")
            print("-------------------------------\n")
            jogadores_aux = []
            total_cerebros_aux = []
            print("Irão desempatar:")
            for n in range(len(vencedor)):
                print(jogadores[vencedor[n]])
                jogadores_aux.append(jogadores[vencedor[n]])
                total_cerebros_aux.append(total_cerebros[vencedor[n]])
                qtd_jogadores = len(vencedor)
            jogadores = jogadores_aux
            total_cerebros = total_cerebros_aux
            print("\n")
        else:
            print("Temos o grande nome de ZOMBIE DICE")
            print("########################################")
            print("{:^40}".format(jogadores[vencedor[0]].upper()))
            print("########################################")
            print(f"Parabéns {jogadores[vencedor[0]]}. Você devorou {maior_cerebro} cérebros.\n")
            print(total_cerebros)
            fim_jogo = True

print("\nFim do jogo.")
