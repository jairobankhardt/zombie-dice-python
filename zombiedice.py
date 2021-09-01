# PONTIFÍCIA UNIVERSIDADE CATÓLICA DO PARANÁ
# ESCOLA POLITÉCNICA
# ANÁLISE E DESENVOLVIMENTO DE SISTEMAS
# RACIOCÍNIO COMPUTACIONAL
# JAIRO MOISÉS STUEHLER BANKHARDT
# IMPLEMENTAÇÃO DO JOGO ZOMBIE DICE

import random
from time import sleep
from collections import namedtuple


#  ***  DEFINIÇÕES E INCREMENTOS  ***  #

def inicializa_copo():
    """
    Inicializa o copo com todos os 13 dados.
    São 6 dados verdes, 4 amarelos e 3 vermelhos.

    :return: lista completa dos dados com suas cores do copo
    """
    return ['verde', 'verde', 'verde', 'verde', 'verde', 'verde',
            'amarelo', 'amarelo', 'amarelo', 'amarelo',
            'vermelho', 'vermelho', 'vermelho']


def pega_cor(cor_fonte, cor_fundo=''):
    """
    Define cores para colorir os textos.

    :param cor_fonte: cor da fonte
    :param cor_fundo: cor de fundo
    :return: o código das cores escolhidas
    """
    fg = {'branco': 30, 'vermelho': 31, 'verde': 32, 'amarelo': 33,
          'azul': 34, 'magenta': 35, 'cyan': 36, 'cinza': 37, 'cinza escuro': 90,
          'vermelho claro': 91, 'verde claro': 92, 'amarelo claro': 93,
          'azul claro': 94, 'magenta claro': 95, 'cyan claro': 96}
    bg = {'branco': 40, 'vermelho': 41, 'verde': 42, 'amarelo': 43,
          'azul': 44, 'magenta': 45, 'cyan': 46, 'cinza': 47, 'cinza escuro': 100,
          'vermelho claro': 101, 'verde claro': 102, 'amarelo claro': 103,
          'azul claro': 104, 'magenta claro': 105, 'cyan claro': 106}
    fundo = ''
    if cor_fundo:
        fundo = f';{bg[cor_fundo]}'

    return '\033[1;'+str(fg[cor_fonte])+fundo+'m'


def finaliza_cor():
    """
    Reseta as cores do texto.

    :return: código para resetar o texto
    """
    return '\033[0;0m'


def incrementa_contadores(face_do_dado, lista_contadores):
    """
    Incrementa os contadores de cérebro, passo e tiro da rodada.

    :param face_do_dado: a face do dado
    :param lista_contadores: a lista dos contadores
    :return: a lista de contadores atualizada
    """
    if face_do_dado == 'cérebro':
        lista_contadores['contC'] += 1
    elif face_do_dado == 'tiro':
        lista_contadores['contT'] += 1
    else:
        lista_contadores['contP'] += 1


def define_jogadores():
    """
    Inicializa a lista de jogadores.

    :return: lista de listas com o nome dos jagadores e 0 para seus cérebros
    """
    qtd = 0
    jog = list()  # lista que irá conter o nome dos jogadores e o número de cérebros
    print('Primeiro vamos conhecer os jogadores.\n')
    while True:
        qtd += 1
        jog.append([input(f'Qual o nome do Jogador número {qtd}? '), 0])
        if qtd >= 2:
            if not quer_continuar('Alguém mais vai jogar?'):
                break
    print('\n')
    return jog


def dormir(segundos, pontos):
    for _ in range(pontos):
        print('. ', end='')
        sleep(segundos)


#  ***  MANIPULAÇÃO DOS DADOS  ***  #

def sorteia_dado_copo(dados_no_copo):
    """
    Sorteia um dado entre os disponíveis no copo

    :param dados_no_copo: lista contendo os dados no copo
    :return: dado sorteado
    """
    return dados_no_copo[random.randrange(len(dados_no_copo))]


def retira_dado_sorteado_do_copo(cor_dado, dados_no_copo):
    """
    Remove um dado do copo.

    :param cor_dado: cor do dado
    :param dados_no_copo: lista de dados do copo
    :return: copo atualizado com menos um dado
    """
    dados_no_copo.remove(cor_dado)


def sorteia_face_do_dado(fc):
    """
    Sorteia a face de um dado.

    :param fc: faces do dado
    :return: face do dado
    """
    return random.choice(fc)


#  ***  EXIBIÇÕES  ***  #

def mostra_copo(dados_copo):
    """
    Mostra os dados que estão no copo.

    :param dados_copo: lista de dados no copo
    :return: Saída com as cores dos dados no copo
    """
    print('Copo: ', end='')
    for c in dados_copo:
        print(f'{pega_cor(c)}{c}{finaliza_cor()} | ', end='')
    print('')


def mostra_dado_sorteado(indice, lista_dados_sorteados):
    """
    Mostra o dado sorteado com a sua face.

    :param indice: a ordem do dado sorteado (0, 1 ou 2)
    :param lista_dados_sorteados: a lista dos dados sorteados
    :return: Exibe mensagem com a ordem, a cor e a face do dado sorteado
    """
    print(f'*** O dado número {indice + 1} '
          f'é de cor {pega_cor(lista_dados_sorteados.cor)}{lista_dados_sorteados.cor:^10}{finaliza_cor()} '
          f'e caiu um {lista_dados_sorteados.face.upper():^10}. ***')


def mostra_contadores(lista_contadores):
    """
    Exibe os contadores de cérebro, passo e tiro da rodada.

    :param lista_contadores: a lista dos contadores
    :return: Mensagem exibindo os valores dos contadores
    """
    print(f'\033[1;35m----- Cérebros: {lista_contadores["contC"]} ----- '
          f'Passos: {lista_contadores["contP"]} ----- '
          f'Tiros: {lista_contadores["contT"]} -----\033[0;0m')


def mostra_contagem_cerebros(lista_jogadores):
    """
    Mostra a contagem total de cérebros dos jogadores.

    :param lista_jogadores: lista dos jogadores
    :return: Exibe a contagem de cérebro total da lista de jogadores
    """
    print('C o n t a g e m   d e   c é r e b r o s')
    for k in range(len(lista_jogadores)):
        print(f'{lista_jogadores[k][0]+" ":.<36} {lista_jogadores[k][1]}')
        sleep(0.7)


def mostra_dados_elegiveis(qtd_passos, qtd_dados_copo):
    """
    Exibe os dados que são possíveis serem rolados na próxima rodada

    :param qtd_passos: quantidade passos da rodada
    :param qtd_dados_copo: quantidade de dados no copo
    :return: Imprime na tela a quantidade de dados elegíveis para a próxima rodada.
    """
    print(f'Dados elegíveis: {qtd_passos + qtd_dados_copo} >>> '
          f'{qtd_dados_copo} dados no copo + {qtd_passos} passos')


def mostra_cerebros_jogador(cerebro_jogador, conta_cerebro):
    """
    Mostra os cérebros que o jogador já possui e os cérebros que ele terá se parar seu turno.

    :param cerebro_jogador: quantidade de cérebros do jogador
    :param conta_cerebro: quantidade de cérebros conquistados no turno até o momento
    :return: Exibe mensagem com a estimativa de cérebros
    """
    print(f'Total de cérebros devorados: de {cerebro_jogador} '
          f'para {cerebro_jogador+conta_cerebro}')


#  ***  VERIFICAÇÕES  ***  #

def quer_continuar(msg):
    """
    Bloco de continuação com mensagem definida como parâmetro.

    :param msg: Texto para exibir na interação com o usuário.
    :return: Verdadeiro ou Falso
    """
    condicao = str(input(f'{msg} (S/N) '))
    while condicao not in 'sSnN':
        print(f'{pega_cor("vermelho claro")}Opção inválida. '
              f'Digite S para Sim ou N para Não. {finaliza_cor()}', end='')
        condicao = str(input(f'{msg} (S/N) '))
    if condicao in 'nN':
        return False
    else:
        return True


def tem_cerebros_suficientes_para_o_final(jdrs):
    """
    Verifica se o número de cérebros para finalizar o jogo foi atingido ou ultrapassado.

    :param jdrs: lista dos jogadores
    :return: Verdadeiro ou falso e o número da maior contagem de cérebros alcançados
    """
    aux = list()
    for x in jdrs:
        aux.append(x[1])
    maior_cerebro = max(aux)
    if maior_cerebro >= CEREBROS_VITORIOSOS:
        return True, maior_cerebro
    else:
        return False, maior_cerebro


def verifica_empate(jdrs, cerebro_maximo):
    """
    Verifica se houve ou não empate e retorna o ou os vencedores.

    :param jdrs: lista dos jogadores
    :param cerebro_maximo:
    :return: Verdadeiro ou Falso e lista dos jogadores que alcançaram a maior pontuação de cérebros.
    """
    vencedor = []
    for j in jdrs:
        if j[1] == cerebro_maximo:
            vencedor.append(j)
    if len(vencedor) > 1:  # Houve empate e terá um novo turno de desempate
        return True, vencedor
    else:
        return False, vencedor


def levou_muitos_tiros(conta_tiros, limite_tiros):
    """
    Verifica se o jogador recebeu muitos tiros quantos necessário para interromper seu turno.

    :param conta_tiros: quantidade de tiros da rodada
    :param limite_tiros: limite de tiros para parar o turno
    :return: Verdadeiro ou Falso para a condição.
    """
    if conta_tiros >= limite_tiros:
        return True
    else:
        return False


def tem_dados_suficientes(conta_passos, qtd_dados_copo, qtd_dados_sortear):
    if conta_passos + qtd_dados_copo < qtd_dados_sortear:
        return False
    else:
        return True


"""

  P R O G R A M A   P R I N C I P A L
  
"""


# INICIALIZAÇÃO DE VARIÁVEIS
TIROS_MATADORES = 3
CEREBROS_VITORIOSOS = 13
DADOS_PARA_SORTEAR = 3
dados_cor = namedtuple('dados_cor', 'verde amarelo vermelho')
dado = dados_cor(('cérebro', 'passo', 'cérebro', 'tiro', 'passo', 'cérebro'),
                 ('tiro', 'passo', 'cérebro', 'tiro', 'passo', 'cérebro'),
                 ('tiro', 'passo', 'tiro', 'cérebro', 'passo', 'tiro'))

# Cabeçalho. Título do jogo.
print('')
print('=' * 60)
print(f'{"Z  O  M  B  I  E     D  I  C  E":^60}')
print('=' * 60)
print('\nVamos começar.')

# Define os jogadores da partida.
jogadores = define_jogadores()

# INÍCIO DO JOGO
while True:
    # Inicializa o turno e o incrementa.
    if 'turno' not in locals():
        turno = 1
    else:
        turno += 1
    print('-' * 50)
    print(f'{"TURNO NÚMERO " + str(turno):^50}')
    print('-' * 50)
    print('\n')

    # Inicia o turno para cada jogador na sequência
    for cont_jog in range(len(jogadores)):
        copo = inicializa_copo()

        # Contadores auxiliares de cérebros, tiros e passos
        contadores = {'contC': 0, 'contT': 0, 'contP': 0}

        # Guardará a cor e face dos dados sorteados da rodada
        cor_face = namedtuple('cor_face', 'cor face')
        dados_sorteados = {'dado1': cor_face('', ''),
                           'dado2': cor_face('', ''),
                           'dado3': cor_face('', '')}

        # Exibe o nome do jogador que está jogando.
        print(f'{pega_cor("cyan")}{" É a vez de " + jogadores[cont_jog][0].upper() + " ":~^50}{finaliza_cor()}')
        print(f'{"Você está com " + str(jogadores[cont_jog][1]) + " cérebros.":^50}\n')

        # INÍCIO DO TURNO
        while True:
            for i, d in enumerate(dados_sorteados):
                # Sorteia dados do copo para os dados que não viraram PASSOS na rodada anterior
                cor_do_dado = ''
                if dados_sorteados[d].face != 'passo':
                    cor_do_dado = sorteia_dado_copo(copo)
                    retira_dado_sorteado_do_copo(cor_do_dado, copo)
                else:
                    # Se tiver um PASSO na rodada anterior, esse dado será re-rolado.
                    cor_do_dado = dados_sorteados[d].cor

                # Sorteia a face do dado conforme a sua cor
                face_dado = sorteia_face_do_dado(dado.__getattribute__(cor_do_dado))

                # Registra e exibe a cor e a face do dado sorteado
                dados_sorteados[d] = cor_face(cor_do_dado, face_dado)
                mostra_dado_sorteado(i, dados_sorteados[d])

                # Incrementa os contadores de cérebro, passos e tiros da rodada
                incrementa_contadores(dados_sorteados[d].face, contadores)

            # Exibe contadores, dados que estão no copo, os dados possíveis para serem jogados e contador de cérebros.
            mostra_contadores(contadores)
            mostra_copo(copo)
            mostra_dados_elegiveis(contadores['contP'], len(copo))
            mostra_cerebros_jogador(jogadores[cont_jog][1], contadores["contC"])

            # VERIFICA SE É POSSÍVEL CONTINUAR O TURNO
            if levou_muitos_tiros(contadores['contT'], TIROS_MATADORES):
                # Levou tantos tiros ou mais do que o permitido para continuar
                print(f'{pega_cor("vermelho claro")}Você recebeu muitos tiros [{contadores["contT"]}].{finaliza_cor()} '
                      f'Seu turno acabou e você não somou cérebros.')
                dormir(0.3, 5)
                print('\n')
                break
            elif not tem_dados_suficientes(contadores['contP'], len(copo), DADOS_PARA_SORTEAR):
                # Não há mais dados suficientes para jogar novamente
                print(f'{pega_cor("vermelho claro")}Número de dados insuficientes para uma nova rodada. '
                      f'[{contadores["contP"] + len(copo)}].{finaliza_cor()}')
                print('Cérebros contabilizados e turno finalizado.')
                jogadores[cont_jog][1] += contadores['contC']
                dormir(0.3, 5)
                print('\n')
                break
            else:
                if not quer_continuar('Você quer jogar novamente neste turno?'):
                    jogadores[cont_jog][1] += contadores['contC']  # incrementa os cérebros deste turno
                    print('\n')
                    break
                else:  # Quer continuar a lançar os dados neste turno
                    contadores['contP'] = 0
                    print('')

    # VERIFICA SE CHEGAMOS AO FIM DO JOGO E SE HOUVE EMPATE
    cerebros_final = tem_cerebros_suficientes_para_o_final(jogadores)
    if cerebros_final[0]:
        empatou = verifica_empate(jogadores, cerebros_final[1])
        if empatou[0]:
            mostra_contagem_cerebros(jogadores)
            print(f'\n{pega_cor("amarelo")}')
            print('#' * 30)
            print(f'{"TEMOS UM EMPATE":^30}')
            print('#' * 30)
            print(f'{finaliza_cor()}', end='')
            print(f'Cérebros degustados: {cerebros_final[1]}')
            print('' * 18)
            print('\nIrão desempatar:')
            mostra_contagem_cerebros(empatou[1])
            jogadores = empatou[1]
            dormir(0.3, 5)
            print('\n')
        else:
            # FIM DO JOGO
            print('Temos o grande nome de ZOMBIE DICE\n')
            print(f'{pega_cor("amarelo claro", "cinza escuro")}{" ":60}{finaliza_cor()}')
            print(f'{pega_cor("amarelo claro", "cinza escuro")}{empatou[1][0][0]:^60}{finaliza_cor()}')
            print(f'{pega_cor("amarelo claro", "cinza escuro")}{" ":60}{finaliza_cor()}')
            print(f'Parabéns {empatou[1][0][0]}. Você devorou {empatou[1][0][1]} cérebros.\n')
            mostra_contagem_cerebros(jogadores)
            break

print('\n\nFIM DO JOGO')
