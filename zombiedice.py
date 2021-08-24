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
DADOS_PARA_SORTEAR = 3
dados = {'\033[1;32mverde\033[0;0m': ('cérebro', 'passo', 'cérebro', 'tiro', 'passo', 'cérebro'),
         '\033[1;33mamarelo\033[0;0m': ('tiro', 'passo', 'cérebro', 'tiro', 'passo', 'cérebro'),
         '\033[1;31mvermelho\033[0;0m': ('tiro', 'passo', 'tiro', 'cérebro', 'passo', 'tiro')}

jogadores = []  # lista que irá conter o nome dos jogadores
total_cerebros = []  # Contador de cérebros degustados pelos jogadores
turno = 0
qtd_jogadores = 0
mais_um_jogador = 'S'
fim_jogo = False

# INÍCIO DO JOGO
print('')
print('=-' * 30)
print(f'{"Z  O  M  B  I  E     D  I  C  E":^60}')
print('=-' * 30)
print('\nVamos começar.')

# JOGADORES - QUANTIDADE E NOMES
print('Primeiro vamos conhecer os jogadores.\n')
while mais_um_jogador == 'S':
    qtd_jogadores += 1
    total_cerebros.append(0)
    jogadores.append(input(f'Qual o nome do Jogador número {qtd_jogadores}? '))
    if qtd_jogadores >= 2:
        mais_um_jogador = input('Alguém mais vai jogar? (S/N) ').upper()
        while mais_um_jogador != 'S' and mais_um_jogador != 'N':
            print('Opção inválida. Digite S para Sim ou N para Não. ', end='')
            mais_um_jogador = input('Alguém mais vai jogar? (S/N) ').upper()
print('\n')

while not fim_jogo:
    turno += 1
    print('-' * 50)
    print(f'{"TURNO NÚMERO " + str(turno):^50}')
    print('-' * 50)
    print('\n')

    for cont_jog in range(qtd_jogadores):
        contC = contT = contP = 0  # Contadores auxiliar de cérebros, tiros e passos
        copo = ['\033[1;32mverde\033[0;0m', '\033[1;32mverde\033[0;0m', '\033[1;32mverde\033[0;0m',
                '\033[1;32mverde\033[0;0m', '\033[1;32mverde\033[0;0m', '\033[1;32mverde\033[0;0m',
                '\033[1;33mamarelo\033[0;0m', '\033[1;33mamarelo\033[0;0m',
                '\033[1;33mamarelo\033[0;0m', '\033[1;33mamarelo\033[0;0m',
                '\033[1;31mvermelho\033[0;0m', '\033[1;31mvermelho\033[0;0m', '\033[1;31mvermelho\033[0;0m']
        fim_turno = False
        dados_sorteados = [['', ''], ['', ''], ['', '']]  # Guardará a cor e face dos dados sorteados

        print(f'\033[1;36m{" É a vez de " + jogadores[cont_jog].upper() + " ":~^50}\033[0;0m')
        print(f'{"Você está com " + str(total_cerebros[cont_jog]) + " cérebros.":^50}\n')

        while not fim_turno:
            for i in range(DADOS_PARA_SORTEAR):
                # Sorteia dados do copo para os dados que não viraram PASSOS na rodada anterior
                # Se tiver um PASSO na rodada anterior, esse dado será re-rolado.
                if dados_sorteados[i][1] != 'passo':
                    indice_copo = random.randrange(len(copo))  # Sorteia um dado do copo
                    dados_sorteados[i][0] = copo[indice_copo]
                    copo.pop(indice_copo)  # Retira o dado do copo

                # Sorteia a face do dado
                dados_sorteados[i][1] = random.choice(dados[dados_sorteados[i][0]])

                # Incrementa contadores
                if dados_sorteados[i][1] == 'cérebro':
                    contC += 1
                elif dados_sorteados[i][1] == 'tiro':
                    contT += 1
                else:
                    contP += 1
                print(f'*** O dado número {i+1} é de cor {dados_sorteados[i][0]:^21} '
                      f'e caiu um {dados_sorteados[i][1].upper():^10}. ***')

            print(f'\033[1;34m----- Cérebros: {contC} ----- Passos: {contP} ----- Tiros: {contT} -----\033[0;0m')
            print('Copo: ', end='')
            for c in copo:
                print(f'{c} | ', end='')
            print(f'\nDados elegíveis: {contP + len(copo)} >>> {len(copo)} dados no copo + {contP} passos')
            print(f'Total de cérebros devorados: de {total_cerebros[cont_jog]} para {total_cerebros[cont_jog]+contC}')

            # VERIFICA SE É POSSÍVEL CONTINUAR O TURNO
            if contT >= TIROS_MATADORES:  # Levou tantos tiros ou mais do que o permitido para continuar
                print(f'Você recebeu muitos tiros [{contT}]. Seu turno acabou e você não somou cérebros.\n\n')
                fim_turno = True
            elif contP + len(copo) < 3:  # Não há mais dados suficientes para jogar novamente
                print(f'Número de dados insuficientes para uma nova rodada. [{contP + len(copo)}].')
                print('Cérebros contabilizados e turno finalizado.\n\n')
                total_cerebros[cont_jog] += contC
                fim_turno = True
            else:
                jogar_novamente = input('Você quer jogar novamente neste turno? (S/N) ').upper()
                while jogar_novamente != 'S' and jogar_novamente != 'N':
                    print('Opção inválida. Digite S para Sim ou N para Não. ', end='')
                    jogar_novamente = input('Você quer jogar novamente neste turno? (S/N) ').upper()
                if jogar_novamente == 'N':  # Não deseja continuar a jogar neste turno
                    total_cerebros[cont_jog] += contC
                    print('\n')
                    fim_turno = True
                else:  # Quer continuar a lançar os dados neste turno
                    contP = 0
                    print('')

    # VERIFICA SE CHEGAMOS AO FIM DO JOGO E SE HOUVE EMPATE
    maior_cerebro = max(total_cerebros)
    if maior_cerebro >= CEREBROS_VITORIOSOS:
        vencedor = []
        for n in range(len(total_cerebros)):
            if total_cerebros[n] == maior_cerebro:
                vencedor.append(n)
        if len(vencedor) > 1:  # Houve empate e terá um novo turno de desempate
            print('' * 18)
            print('TEMOS UM EMPATE.')
            print(f'Cérebros degustados: {total_cerebros}')
            print('' * 18)
            jogadores_aux = []
            total_cerebros_aux = []
            print('\nIrão desempatar:')
            for n in range(len(vencedor)):
                print(jogadores[vencedor[n]])
                jogadores_aux.append(jogadores[vencedor[n]])
                total_cerebros_aux.append(total_cerebros[vencedor[n]])
                qtd_jogadores = len(vencedor)
            jogadores = jogadores_aux
            total_cerebros = total_cerebros_aux
            print('\n')
        else:
            print('Temos o grande nome de ZOMBIE DICE\n')
            print(f'\033[1;93;100m{" ":60}\033[0;0m')
            print(f'\033[1;93;100m{jogadores[vencedor[0]].upper():^60}\033[0;0m')
            print(f'\033[1;93;100m{" ":60}\033[0;0m')
            # print('#' * 40)
            print(f'Parabéns {jogadores[vencedor[0]]}. Você devorou {maior_cerebro} cérebros.\n')
            print('C o n t a g e m   d e   c é r e b r o s')
            for n in range(len(jogadores)):
                print(f'{jogadores[n]:.<36} {total_cerebros[n]}')
            fim_jogo = True

print('\n\nFIM DO JOGO')
