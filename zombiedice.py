# PONTIFÍCIA UNIVERSIDADE CATÓLICA DO PARANÁ
# ESCOLA POLITÉCNICA
# ANÁLISE E DESENVOLVIMENTO DE SISTEMAS
# RACIOCÍNIO COMPUTACIONAL
# JAIRO MOISÉS STUEHLER BANKHARDT
# IMPLEMENTAÇÃO DO JOGO ZOMBIE DICE

import random
from time import sleep
from collections import namedtuple


class Dados:

    def __init__(self):
        self.__dados_cor = namedtuple('dados_cor', 'verde amarelo vermelho')
        self.__dado = self.__dados_cor(('cérebro', 'passo', 'cérebro', 'tiro', 'passo', 'cérebro'),
                                       ('tiro', 'passo', 'cérebro', 'tiro', 'passo', 'cérebro'),
                                       ('tiro', 'passo', 'tiro', 'cérebro', 'passo', 'tiro'))
        self.__copo = list()
        self.__dados_sorteados = {}

        self.__cor_face = namedtuple('cor_face', 'cor face')

    def get_copo(self):
        return self.__copo

    def get_dado(self):
        return self.__dado

    def get_dados_sorteados(self):
        return self.__dados_sorteados

    def set_dados_sorteados(self, i, cor, face):
        self.__dados_sorteados[i] = self.__cor_face(cor, face)

    def inicializa_copo(self):
        """
        Inicializa o copo com todos os 13 dados.
        São 6 dados verdes, 4 amarelos e 3 vermelhos.

        :return: lista completa dos dados com suas cores do copo
        """
        self.__copo = ['verde', 'verde', 'verde', 'verde', 'verde', 'verde',
                       'amarelo', 'amarelo', 'amarelo', 'amarelo',
                       'vermelho', 'vermelho', 'vermelho']

    def inicializa_dados_sorteados(self):
        """
        Limpa o dicionário referente aos dados sorteados.
        :return: Dicionário com 3 dados vazios.
        """
        self.__dados_sorteados = {'dado1': self.__cor_face('', ''),
                                  'dado2': self.__cor_face('', ''),
                                  'dado3': self.__cor_face('', '')}

    def sorteia_dado_copo(self):
        """
        Sorteia um dado entre os disponíveis no copo

        :return: dado sorteado (a cor)
        """
        return self.__copo[random.randrange(len(self.__copo))]

    def retira_dado_sorteado_do_copo(self, cor_dado):
        """
        Remove um dado do copo.

        :param cor_dado: cor do dado
        :return: copo atualizado com menos um dado
        """
        self.__copo.remove(cor_dado)

    def sorteia_face_do_dado(self, cor):
        """
        Sorteia a face de um dado na cor correspondente ao parâmetro.

        :param cor: cor do dado
        :return: face do dado
        """
        return random.choice(self.get_dado().__getattribute__(cor))

    def mostra_copo(self):
        """
        Mostra os dados que estão no copo.

        :return: Saída com com o nome das cores dos dados no copo
        """
        tinta = Cores()
        cont = 1
        print('Copo: ', end='')
        for cor in self.__copo:
            print(f'{tinta.pega_cor(cor)}{cor}{tinta.finaliza_cor()} / ', end='')
            cont += 1
        print('')

    @staticmethod
    def mostra_dado_sorteado(i, dado_sort):
        """
        Mostra o dado sorteado com a sua face.

        :param i: a ordem do dado sorteado (0, 1 ou 2)
        :param dado_sort: o dado sorteado
        :return: Exibe mensagem com a ordem, a cor e a face do dado sorteado
        """
        tinta = Cores()
        print(f'*** O dado número {i + 1} '
              f'é de cor {tinta.pega_cor(dado_sort.cor)}'
              f'{dado_sort.cor:^10}{tinta.finaliza_cor()} '
              f'e caiu um {dado_sort.face.upper():^10}. ***')

    @staticmethod
    def mostra_dados_elegiveis(qtd_passos, qtd_dados_copo):
        """
        Exibe a quantidade de dados possíveis de serem rolados na próxima rodada

        :param qtd_passos: quantidade passos da rodada
        :param qtd_dados_copo: quantidade de dados no copo
        :return: Imprime na tela a quantidade de dados elegíveis para a próxima rodada.
        """
        print(f'Dados elegíveis: {qtd_passos + qtd_dados_copo} >>> '
              f'{qtd_dados_copo} dados no copo + {qtd_passos} passos')

    @staticmethod
    def tem_dados_suficientes(conta_passos, qtd_dados_copo, qtd_dados_sortear):
        """
        Verifica se há dados suficientes para iniciar nova rodada.

        :param conta_passos: Número de dados da rodada com a face Passo.
        :param qtd_dados_copo: Número de dados no copo.
        :param qtd_dados_sortear: Configuração de dados suficientes para nova jogada.
        :return: Verdadeiro ou Falso.
        """
        if conta_passos + qtd_dados_copo < qtd_dados_sortear:
            return False
        else:
            return True


class Contadores:

    def __init__(self, tiros_matadores=3, cerebros_vitoriosos=13, dados_para_sortear=3):
        self.__tiros_matadores = tiros_matadores
        self.__cerebros_vitoriosos = cerebros_vitoriosos
        self.__dados_para_sortear = dados_para_sortear
        self.__contadores_ctp = {}
        self.__turno = 0

    def get_tiros_matadores(self):
        return self.__tiros_matadores

    def get_cerebros_vitoriosos(self):
        return self.__cerebros_vitoriosos

    def get_dados_para_sortear(self):
        return self.__dados_para_sortear

    def get_contadores_ctp(self):
        return self.__contadores_ctp

    def set_contadores_ctp(self, face_do_dado):
        """
        Incrementa os contadores de cérebro, passo e tiro da rodada.

        :param face_do_dado: a face do dado
        :return: a lista de contadores atualizada
        """
        if face_do_dado == 'cérebro':
            self.__contadores_ctp['contC'] += 1
        elif face_do_dado == 'tiro':
            self.__contadores_ctp['contT'] += 1
        else:
            self.__contadores_ctp['contP'] += 1

    def get_turno(self):
        return self.__turno

    def set_turno(self, turno):
        self.__turno = turno

    def inicializa_contadores_ctp(self):
        self.__contadores_ctp = {'contC': 0, 'contT': 0, 'contP': 0}

    def mostra_contadores_ctp(self):
        """
        Exibe os contadores de cérebro, passo e tiro da rodada.

        :return: Mensagem exibindo os valores dos contadores
        """
        print(f'\033[1;35m----- Cérebros: {self.get_contadores_ctp()["contC"]} ----- '
              f'Passos: {self.get_contadores_ctp()["contP"]} ----- '
              f'Tiros: {self.get_contadores_ctp()["contT"]} -----\033[0;0m')

    @staticmethod
    def quer_continuar(msg):
        """
        Bloco de continuação com mensagem definida como parâmetro.

        :param msg: Texto para exibir na interação com o usuário.
        :return: Verdadeiro ou Falso
        """
        tinta = Cores()
        condicao = str(input(f'{msg} (S/N) '))
        while condicao not in 'sSnN' or condicao == '':
            print(f'{tinta.pega_cor("vermelho claro")}Opção inválida. '
                  f'Digite S para Sim ou N para Não. {tinta.finaliza_cor()}', end='')
            condicao = str(input(f'{msg} (S/N) ')).upper()
        if condicao in 'nN':
            return False
        else:
            return True

    @staticmethod
    def dormir(segundos, pontos):
        """
        Faz o programa pausar.

        :param segundos: número de segundos para pausar em cada ponto
        :param pontos: número de pontos de pausa
        :return: Exibe pontos de pausa
        """
        for _ in range(pontos):
            print('. ', end='')
            sleep(segundos)


class Jogadores:

    def __init__(self):
        self.__qtd_jogadores = 0
        self.__lista_jogadores = list()  # lista que irá conter o nome dos jogadores e o número de cérebros

    def get_qtd_jogadores(self):
        return self.__qtd_jogadores

    def get_lista_jogadores(self):
        return self.__lista_jogadores

    def set_lista_jogadores(self, lista_jogadores):
        self.__lista_jogadores = lista_jogadores

    def define_jogadores(self):
        """
        Inicializa a lista de jogadores.

        :return: lista de listas com o nome dos jagadores e 0 para seus cérebros
        """
        print('Primeiro vamos conhecer os jogadores.\n')
        while True:
            self.__qtd_jogadores += 1
            self.__lista_jogadores.append([input(f'Qual o nome do Jogador número {self.__qtd_jogadores}? '), 0])
            if self.__qtd_jogadores >= 2:
                if not Contadores.quer_continuar('Alguém mais vai jogar?'):
                    break
        print('\n')

    def mostra_contagem_cerebros(self):
        """
        Mostra a contagem total de cérebros dos jogadores.

        :return: Exibe a contagem de cérebro total da lista de jogadores
        """
        print('C o n t a g e m   d e   c é r e b r o s')
        for k in range(len(self.__lista_jogadores)):
            print(f'{self.__lista_jogadores[k][0] + " ":.<36} {self.__lista_jogadores[k][1]}')
            sleep(0.7)

    @staticmethod
    def mostra_cerebros_jogador(cerebro_jogador, conta_cerebro):
        """
        Mostra os cérebros que o jogador já possui e os cérebros que ele terá se parar seu turno.

        :param cerebro_jogador: quantidade de cérebros do jogador
        :param conta_cerebro: quantidade de cérebros conquistados no turno até o momento
        :return: Exibe mensagem com a estimativa de cérebros
        """
        tinta = Cores()
        print(f'Total de cérebros devorados: {tinta.pega_cor("azul")}de {cerebro_jogador} '
              f'para {cerebro_jogador + conta_cerebro}{tinta.finaliza_cor()}')

    def tem_cerebros_suficientes_para_o_final(self, cerebros_vitoriosos):
        """
        Verifica se o número de cérebros para finalizar o jogo foi atingido ou ultrapassado.

        :param cerebros_vitoriosos: numero de cerebros para ganhar o jogo
        :return: Verdadeiro ou falso e o número da maior contagem de cérebros alcançados
        """
        aux = list()
        for x in self.__lista_jogadores:
            aux.append(x[1])
        maior_cerebro = max(aux)
        if maior_cerebro >= cerebros_vitoriosos:
            return True, maior_cerebro
        else:
            return False, maior_cerebro

    def verifica_empate(self, cerebro_maximo):
        """
        Verifica se houve ou não empate e retorna o ou os vencedores.

        :param cerebro_maximo:
        :return: Verdadeiro ou Falso e lista dos jogadores que alcançaram a maior pontuação de cérebros.
        """
        vencedor = []
        for j in self.__lista_jogadores:
            if j[1] == cerebro_maximo:
                vencedor.append(j)
        if len(vencedor) > 1:  # Houve empate e terá um novo turno de desempate
            return True, vencedor
        else:
            return False, vencedor

    @staticmethod
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


class Cores:

    def __init__(self):
        self.__fg = {'branco': 30, 'vermelho': 31, 'verde': 32, 'amarelo': 33,
                     'azul': 34, 'magenta': 35, 'cyan': 36, 'cinza': 37, 'cinza escuro': 90,
                     'vermelho claro': 91, 'verde claro': 92, 'amarelo claro': 93,
                     'azul claro': 94, 'magenta claro': 95, 'cyan claro': 96}
        self.__bg = {'branco': 40, 'vermelho': 41, 'verde': 42, 'amarelo': 43,
                     'azul': 44, 'magenta': 45, 'cyan': 46, 'cinza': 47, 'cinza escuro': 100,
                     'vermelho claro': 101, 'verde claro': 102, 'amarelo claro': 103,
                     'azul claro': 104, 'magenta claro': 105, 'cyan claro': 106}

    def pega_cor(self, cor_fonte, cor_fundo=''):
        """
        Define cores para colorir os textos.

        :param cor_fonte: cor da fonte
        :param cor_fundo: cor de fundo
        :return: o código das cores escolhidas
        """
        fundo = ''
        if cor_fundo:
            fundo = f';{self.__bg[cor_fundo]}'
        return '\033[1;' + str(self.__fg[cor_fonte]) + fundo + 'm'

    @staticmethod
    def finaliza_cor():
        """
        Reseta as cores do texto.

        :return: código para resetar o texto
        """
        return '\033[0;0m'


"""

  P R O G R A M A   P R I N C I P A L
  
"""


# INICIALIZAÇÃO DE VARIÁVEIS E OBJETOS
dados = Dados()
cores = Cores()
contadores = Contadores(3, 13, 3)
jogadores = Jogadores()

# Cabeçalho. Título do jogo.
print('')
print('=' * 60)
print(f'{"Z  O  M  B  I  E     D  I  C  E":^60}')
print('=' * 60)
print('\nVamos começar.')

# Define os jogadores da partida.
jogadores.define_jogadores()

# INÍCIO DO JOGO
while True:
    # Inicializa o turno e o incrementa.
    contadores.set_turno(contadores.get_turno()+1)
    print('-' * 50)
    print(f'{"TURNO NÚMERO " + str(contadores.get_turno()):^50}')
    print('-' * 50)
    print('\n')

    # Inicia o turno para cada jogador na sequência
    for cont_jog in range(len(jogadores.get_lista_jogadores())):

        # Coloca todos os dados no copo
        dados.inicializa_copo()

        # Contadores auxiliares de cérebros, tiros e passos
        contadores.inicializa_contadores_ctp()

        # Guardará a cor e face dos dados sorteados da rodada
        dados.inicializa_dados_sorteados()

        # Exibe o nome do jogador que está jogando.
        print(f'{cores.pega_cor("cyan")}'
              f'{" É a vez de " + jogadores.get_lista_jogadores()[cont_jog][0].upper() + " ":~^50}'
              f'{cores.finaliza_cor()}')
        print(f'{"Você está com " + str(jogadores.get_lista_jogadores()[cont_jog][1]) + " cérebros.":^50}\n')

        # INÍCIO DO TURNO
        while True:
            for indice, dado in enumerate(dados.get_dados_sorteados()):
                # Sorteia dados do copo para os dados que não viraram PASSOS na rodada anterior
                dado_sorteado_cor = ''
                if dados.get_dados_sorteados()[dado].face != 'passo':
                    dado_sorteado_cor = dados.sorteia_dado_copo()
                    dados.retira_dado_sorteado_do_copo(dado_sorteado_cor)
                else:
                    # Se tiver um PASSO na rodada anterior, esse dado será re-rolado.
                    dado_sorteado_cor = dados.get_dados_sorteados()[dado].cor

                # Sorteia a face do dado conforme a sua cor
                face_dado = dados.sorteia_face_do_dado(dado_sorteado_cor)

                # Registra e exibe a cor e a face do dado sorteado
                dados.set_dados_sorteados(dado, dado_sorteado_cor, face_dado)
                dados.mostra_dado_sorteado(indice, dados.get_dados_sorteados()[dado])

                # Incrementa os contadores de cérebro, passos e tiros da rodada
                contadores.set_contadores_ctp(dados.get_dados_sorteados()[dado].face)

            # Exibe contadores, dados que estão no copo, os dados possíveis para serem jogados e contador de cérebros.
            contadores.mostra_contadores_ctp()
            dados.mostra_copo()
            dados.mostra_dados_elegiveis(contadores.get_contadores_ctp()['contP'], len(dados.get_copo()))
            jogadores.mostra_cerebros_jogador(jogadores.get_lista_jogadores()[cont_jog][1],
                                              contadores.get_contadores_ctp()["contC"])

            # VERIFICA SE É POSSÍVEL CONTINUAR O TURNO
            if jogadores.levou_muitos_tiros(contadores.get_contadores_ctp()['contT'], contadores.get_tiros_matadores()):
                # Levou tantos tiros ou mais do que o permitido para continuar
                print(f'{cores.pega_cor("vermelho claro")}Você recebeu muitos tiros '
                      f'[{contadores.get_contadores_ctp()["contT"]}].{cores.finaliza_cor()} '
                      f'Seu turno acabou e você não somou cérebros.')
                contadores.dormir(0.3, 5)
                print('\n')
                break
            elif not dados.tem_dados_suficientes(contadores.get_contadores_ctp()['contP'],
                                                 len(dados.get_copo()), contadores.get_dados_para_sortear()):
                # Não há mais dados suficientes para jogar novamente
                print(f'{cores.pega_cor("vermelho claro")}Número de dados insuficientes para uma nova rodada. '
                      f'[{contadores.get_contadores_ctp()["contP"] + len(dados.get_copo())}].{cores.finaliza_cor()}')
                print('Cérebros contabilizados e turno finalizado.')
                jogadores.get_lista_jogadores()[cont_jog][1] += contadores.get_contadores_ctp()['contC']
                contadores.dormir(0.3, 5)
                print('\n')
                break
            else:
                if not contadores.quer_continuar('Você quer jogar novamente neste turno?'):
                    # incrementa os cérebros deste turno
                    jogadores.get_lista_jogadores()[cont_jog][1] += contadores.get_contadores_ctp()['contC']
                    print('\n')
                    break
                else:  # Quer continuar a lançar os dados neste turno
                    contadores.get_contadores_ctp()['contP'] = 0
                    print('')

    # VERIFICA SE O JOGO CHEGOU AO FIM OU SE HOUVE EMPATE
    cerebros_final = jogadores.tem_cerebros_suficientes_para_o_final(contadores.get_cerebros_vitoriosos())
    if cerebros_final[0]:
        empatou = jogadores.verifica_empate(cerebros_final[1])
        if empatou[0]:
            jogadores.mostra_contagem_cerebros()
            print(f'\n{cores.pega_cor("amarelo")}')
            print('#' * 30)
            print(f'{"TEMOS UM EMPATE":^30}')
            print('#' * 30)
            print(f'{cores.finaliza_cor()}', end='')
            print(f'Cérebros degustados: {cerebros_final[1]}')
            print('' * 18)
            print('\nIrão desempatar:')
            jogadores.set_lista_jogadores(empatou[1])
            jogadores.mostra_contagem_cerebros()
            contadores.dormir(0.3, 5)
            print('\n')
        else:
            # FIM DO JOGO
            print('Temos o grande nome de ZOMBIE DICE\n')
            print(f'{cores.pega_cor("amarelo claro", "cinza escuro")}{" ":60}{cores.finaliza_cor()}')
            print(f'{cores.pega_cor("amarelo claro", "cinza escuro")}'
                  f'{str(empatou[1][0][0]).upper():^60}{cores.finaliza_cor()}')  # Mostra o nome do vencendor
            print(f'{cores.pega_cor("amarelo claro", "cinza escuro")}{" ":60}{cores.finaliza_cor()}')
            print(f'Parabéns {empatou[1][0][0]}. Você devorou {empatou[1][0][1]} cérebros.\n')
            jogadores.mostra_contagem_cerebros()
            break

print('\n\nFIM DO JOGO')
