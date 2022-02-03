import socket
from game_ import Jogo # Importando a Classe Jogo
import pickle # Módulo para a conversão e envio de dados, byte para objetos e objeto para byte
from _thread import *

porta = 5555 # Porta a ser usada pela aplicação
servidor = '' # Endereço IP do Servidor Linode a ser detectado
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Criação do socket. socket.AF_INET - Comunicação com endereços IPv4
# Tipo do Socket é socket.SOCK_STREAM, o protocolo padrão usado será o TCP.
try:
    s.bind((servidor, porta)) # Vinculando o servidor e a porta em questão ao socket
except socket.error as h:
    str(h)

s.listen() # "Ouvindo", buscando conexões. Podemos ter conexões ilimitadas de uma única vez, ou seja, várias partidas ocorrendo
# ao mesmo tempo
print("Aguardando conexão")

jogos = {} # Dicionário que armazenará todos os ID's dos jogos ocorrendo naquele momento. Key: ID, valor
countID = 0 # Manter um controle dos ID's dos jogos, dois jogos diferentes não podem ter o mesmo ID
conectado = set() # Armazena os endereços IP dos Clients conectados

def client_thread(conex, player, jogoId): # Função para a criação de uma nova thread, client do jogo. p é o player atual (0 ou 1)
    # Para cada client haverá uma função dessa por trás
    global countID # Se alguém se desconectar, será necessário subtrair
    conex.send(str.encode(str(player))) # Envio para o client de qual player ele é, 0 ou 1
    while True:
        try:
            dado = conex.recv(4096).decode() # Constantemente tentando receber dados, quantidade de bytes(4096).
            if jogoId in jogos: # Checando se o jogo ainda existe
                jogo = jogos[jogoId] # Se existe, tentamos chegar se é um "get", "reset" ou um movimento.
                if not dado:
                    break
                else:
                    if dado == "reset": # Quando o jogo enviar "reset", significa que a rodada terminou e será preciso resetar os movimentos
                        jogo.Mov_reset()
                    elif dado != "get": # Se for um movimento(Pedra, Papel ou Tesoura), o mesmo será enviado ao jogo para ser atualizado
                        jogo.jogar(player, dado) # dado será o Movimento feito aqui

                    conex.sendall(pickle.dumps(jogo)) # Empacotamento do jogo para ser enviado ao client. Client receberá e desempacotará
            else:
                break
        except:
            break

    print("Conexão perdida") # Se o loop quebrar...
    try:
        del jogos[jogoId] # Se algum client se desconectar da partida, precisamos deletar aquele jogoId
        print("Fechando jogo", jogoId)
    except:
        pass
    countID -= 1
    conex.close() # Fechando a conexão

procura = True
while procura: # Continuamente procurando conexão. Se um novo player se conectar, uma nova thread será iniciada
    conex, ende = s.accept() # Aceitar conexão, armazena a conexão e o endereço da mesma nas variáveis conex e ende
    print("Conectado a:", ende)
    countID += 1 # Manter controle de quantas pessoas estão conectadas ao servidor naquele momento
    player = 0 # Player 0 ou Player 1
    jogoId = (countID - 1)//2 # A cada duas pessoas que se conectarem ao servidor, o ID do jogo é incrementado em 1
    if countID % 2 == 1: # Se o número de players for ímpar...
        jogos[jogoId] = Jogo(jogoId)
        print("Criando um novo jogo...")
    else: 
        jogos[jogoId].pronto = True
        player = 1

    start_new_thread(client_thread, (conex, player, jogoId))
