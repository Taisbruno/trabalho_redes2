import socket
import pickle # Módulo para a conversão e envio de dados, byte para objetos e objeto para byte

class Network_:
    def __init__(self):
        self.cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.servidor = "69.164.205.232" # Endereço IP do Servidor Linode
        self.porta = 5555 # Porta escolhida para conexão
        self.ende = (self.servidor, self.porta)
        self.pos = self.conectar() # ID que será armazenado nesse network object. Será necessário mandar esse ID 
        # para cada client conectado para que eles saibam quem é player 0 e quem é player 1 daquela partida

    def conectar(self): # Função para conectar ao Client
        try:
            self.cliente.connect(self.ende)
            return self.cliente.recv(2048).decode() # Quando houver a conexão, queremos obter o player number para aquele Cliente
        except:
            pass

    def enviar(self, dado): # Função para envio das informações
        try:
            self.cliente.send(str.encode(dado)) # Envio de uma string encoded para o servidor
            return pickle.loads(self.cliente.recv(4096)) # Recebe de volta e carrega esse objeto de dado retornado
        except socket.error as h:
            print(h)

    def pegar_Pos(self): # Função para pegar a posição de um objeto dentro do Client
        return self.pos
