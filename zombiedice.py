# PONTIFÍCIA UNIVERSIDADE CATÓLICA DO PARANÁ
# ESCOLA POLITÉCNICA
# ANÁLISE E DESENVOLVIMENTO DE SISTEMAS
# RACIOCÍNIO COMPUTACIONAL
# JAIRO MOISÉS STUEHLER BANKHARDT
# IMPLEMENTAÇÃO DO JOGO ZOMBIE DICE

import random
from time import sleep


def inicializa_copo():
    """
    Inicializa o copo com todos os 13 dados.
    São 6 dados verdes, 4 amarelos e 3 vermelhos.

    :return: lista das cores dos dados
    """
    return ['\033[1;32mverde\033[0;0m', '\033[1;32mverde\033[0;0m', '\033[1;32mverde\033[0;0m',
            '\033[1;32mverde\033[0;0m', '\033[1;32mverde\033[0;0m', '\033[1;32mverde\033[0;0m',
            '\033[1;33mamarelo\033[0;0m', '\033[1;33mamarelo\033[0;0m',
            '\033[1;33mamarelo\033[0;0m', '\033[1;33mamarelo\033[0;0m',
            '\033[1;31mvermelho\033[0;0m', '\033[1;31mvermelho\033[0;0m', '\033[1;31mvermelho\033[0;0m']


def sorteia_dado_copo(dados_no_copo):
    """
    Sorteia um dado entre os disponíveis no copo

    :param dados_no_copo: lista contendo os dados no copo
    :return: dado sorteado
    """
    return copo[random.randrange(len(dados_no_copo))]


def retira_dado_sorteado_do_copo(d_sorteado, dados_no_copo):
    """
    Remove um dado do copo.

    :param d_sorteado: cor do dado
    :param dados_no_copo: lista de dados do copo
    :return: copo atualizado com menos um dado
    """
    dados_no_copo.remove(d_sorteado)


def sorteia_face_do_dado(cor_dado):
    """
    Sorteia a face de um dado.

    :param cor_dado: cor do dado para sortear a face
    :return: face do dado
    """
    return random.choice(dados[cor_dado])


def mostra_copo(dados_copo):
    """
    Mostra os dados que estão no copo.

    :param dados_copo: lista de dados no copo
    :return: Saída com as cores dos dados no copo
    """
    print('Copo: ', end='')
    for c in dados_copo:
        print(f'{c} | ', end='')
    print('')


def mostra_dado_sorteado(indice, lista_dados_sorteados):
    """
    Mostra o dado sorteado com a sua face.

    :param indice: a ordem do dado sorteado (1, 2 ou 3)
    :param lista_dados_sorteados: a lista dos dados sorteados
    :return: Exibe a cor e a face do dado sorteado
    """
    print(f'*** O dado número {indice + 1} é de cor {lista_dados_sorteados[indice][0]:^21} '
          f'e caiu um {lista_dados_sorteados[indice][1].upper():^10}. ***')


def incrementa_contadores(face_dado, lista_contadores):
    """
    Incrementa os contadores de cérebro, passo e tiro da rodada.

    :param face_dado: a face do dado
    :param lista_contadores: a lista dos contadores
    :return: a lista de contadores atualizada
    """
    if face_dado == 'cérebro':
        lista_contadores['contC'] += 1
    elif face_dado == 'tiro':
        lista_contadores['contT'] += 1
    else:
        lista_contadores['contP'] += 1
    return lista_contadores


def mostra_contadores(lista_contadores):
    """
    Exibe os contadores de cérebro, passo e tiro da rodada.

    :param lista_contadores: a lista dos contadores
    :return: Saída dos contadores
    """
    print(f'\033[1;35m----- Cérebros: {lista_contadores["contC"]} ----- '
          f'Passos: {lista_contadores["contP"]} ----- '
          f'Tiros: {lista_contadores["contT"]} -----\033[0;0m')


def mostra_contagem_cerebros(contagem_cerebros, lista_jogadores):
    """
    Mostra a contagem total de cérebros dos jogadores.

    :param contagem_cerebros: lista do contador de cérebro
    :param lista_jogadores: lista dos jogadores
    :return: Exibe a contagem de cérebro total
    """
    print('C o n t a g e m   d e   c é r e b r o s')
    for k in range(len(lista_jogadores)):
        print(f'{lista_jogadores[k]+" ":.<36} {contagem_cerebros[k]}')


# INICIALIZAÇÃO DE VARIÁVEIS
TIROS_MATADORES = 3
CEREBROS_VITORIOSOS = 5
DADOS_PARA_SORTEAR = 3
dados = {'\033[1;32mverde\033[0;0m': ('cérebro', 'passo', 'cérebro', 'tiro', 'passo', 'cérebro'),
         '\033[1;33mamarelo\033[0;0m': ('tiro', 'passo', 'cérebro', 'tiro', 'passo', 'cérebro'),
         '\033[1;31mvermelho\033[0;0m': ('tiro', 'passo', 'tiro', 'cérebro', 'passo', 'tiro')}

# CABEÇALHO. TÍTULO DO JOGO.
print('')
print('=' * 60)
print(f'{"Z  O  M  B  I  E     D  I  C  E":^60}')
print('=' * 60)
print('\nVamos começar.')

# JOGADORES - QUANTIDADE E NOMES
mais_um_jogador = 'S'
qtd_jogadores = 0
jogadores = []  # lista que irá conter o nome dos jogadores
total_cerebros = []  # Contador de cérebros degustados pelos jogadores
print('Primeiro vamos conhecer os jogadores.\n')
while mais_um_jogador == 'S':
    qtd_jogadores += 1
    total_cerebros.append(0)
    jogadores.append(input(f'Qual o nome do Jogador número {qtd_jogadores}? '))
    if qtd_jogadores >= 2:
        mais_um_jogador = input('Alguém mais vai jogar? (S/N) ').upper()
        while mais_um_jogador not in 'sSnN':
            print('\033[1;91mOpção inválida. Digite S para Sim ou N para Não. \033[0;0m', end='')
            mais_um_jogador = input('Alguém mais vai jogar? (S/N) ').upper()
print('\n')

# INÍCIO DO JOGO
# turno = 0
while True:
    if 'turno' not in locals():
        turno = 1
    else:
        turno += 1
    print('-' * 50)
    print(f'{"TURNO NÚMERO " + str(turno):^50}')
    print('-' * 50)
    print('\n')

    for cont_jog in range(qtd_jogadores):
        copo = inicializa_copo()
        # Contadores auxiliar de cérebros, tiros e passos
        contadores = {'contC': 0, 'contT': 0, 'contP': 0}
        # Guardará a cor e face dos dados sorteados
        dados_sorteados = [['', ''], ['', ''], ['', '']]

        print(f'\033[1;36m{" É a vez de " + jogadores[cont_jog].upper() + " ":~^50}\033[0;0m')
        print(f'{"Você está com " + str(total_cerebros[cont_jog]) + " cérebros.":^50}\n')

        # INÍCIO DO TURNO
        while True:
            for i in range(DADOS_PARA_SORTEAR):
                # Sorteia dados do copo para os dados que não viraram PASSOS na rodada anterior
                # Se tiver um PASSO na rodada anterior, esse dado será re-rolado.
                if dados_sorteados[i][1] != 'passo':
                    dado_sorteado = sorteia_dado_copo(copo)
                    retira_dado_sorteado_do_copo(dado_sorteado, copo)
                    dados_sorteados[i][0] = dado_sorteado

                # Sorteia a face do dado
                dados_sorteados[i][1] = sorteia_face_do_dado(dados_sorteados[i][0])

                mostra_dado_sorteado(i, dados_sorteados)

                # Incrementa os contadores de cérebro, passos e tiros da rodada
                contadores = incrementa_contadores(dados_sorteados[i][1], contadores)

            mostra_contadores(contadores)
            mostra_copo(copo)

            print(f'Dados elegíveis: {contadores["contP"] + len(copo)} >>> '
                  f'{len(copo)} dados no copo + {contadores["contP"]} passos')
            print(f'Total de cérebros devorados: de {total_cerebros[cont_jog]} '
                  f'para {total_cerebros[cont_jog]+contadores["contC"]}')

            # VERIFICA SE É POSSÍVEL CONTINUAR O TURNO
            if contadores['contT'] >= TIROS_MATADORES:
                # Levou tantos tiros ou mais do que o permitido para continuar
                print(f'Você recebeu muitos tiros [{contadores["contT"]}]. '
                      f'Seu turno acabou e você não somou cérebros.\n\n')
                sleep(1)
                break
            elif contadores['contP'] + len(copo) < 3:
                # Não há mais dados suficientes para jogar novamente
                print(f'Número de dados insuficientes para uma nova rodada. [{contadores["contP"] + len(copo)}].')
                print('Cérebros contabilizados e turno finalizado.\n\n')
                total_cerebros[cont_jog] += contadores['contC']
                sleep(1)
                break
            else:
                jogar_novamente = input('Você quer jogar novamente neste turno? (S/N) ').upper()
                while jogar_novamente != 'S' and jogar_novamente != 'N':
                    print('\033[1;91mOpção inválida. Digite S para Sim ou N para Não. \033[0;0m', end='')
                    jogar_novamente = input('Você quer jogar novamente neste turno? (S/N) ').upper()
                if jogar_novamente == 'N':  # Não deseja continuar a jogar neste turno
                    total_cerebros[cont_jog] += contadores['contC']  # incrementa os cérebros deste turno
                    print('\n')
                    break
                else:  # Quer continuar a lançar os dados neste turno
                    contadores['contP'] = 0
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
            sleep(1)
            print('\n')
        else:
            # FIM DO JOGO
            print('Temos o grande nome de ZOMBIE DICE\n')
            print(f'\033[1;93;100m{" ":60}\033[0;0m')
            print(f'\033[1;93;100m{jogadores[vencedor[0]].upper():^60}\033[0;0m')
            print(f'\033[1;93;100m{" ":60}\033[0;0m')
            print(f'Parabéns {jogadores[vencedor[0]]}. Você devorou {maior_cerebro} cérebros.\n')
            mostra_contagem_cerebros(total_cerebros, jogadores)
            break

print('\n\nFIM DO JOGO')
