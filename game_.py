class Jogo:
    def __init__(self, id):
        self.p1Mov = False # Se player 1 fez algum movimento
        self.p2Mov = False # Se player 2 fez algum movimento
        self.pronto = False
        self.id = id # Cada jogo criado terá um único ID numérico para determinar quais clients fazem parte de qual jogo.
        self.movs = [None, None]
        self.vence = [0,0] # Player 0 e Player 1
        self.empate = 0

    def conectado(self): # Verificar se os dois jogadores da partida estão conectados
        return self.pronto

    def jogar(self, player, mov):
        self.movs[player] = mov
        if player == 0:
            self.p1Mov = True
        else:
            self.p2Mov = True

    def Mov_All(self): # Se ambos os jogadores já fizeram algum movimento
        return self.p1Mov and self.p2Mov

    def Mov_reset(self): # Resetar os movimentos de cada Player para a próxima rodada
        self.p1Mov = False
        self.p2Mov = False

    def pegar_Mov(self, player): # Identificar movimento do Player
        return self.movs[player] # 0 representa Player 1 e 1 representa Player 2

    def vencedor(self): # Qual player é o vencedor daquela rodada baseado nas escolhas de cada um, Pedra, Papel ou Tesoura
        player1 = self.movs[0].upper()[0:2] # Pegar as duas primeiras letras do Movimento (Escolha) feita pelo Player 1
        player2 = self.movs[1].upper()[0:2] # Pegar as duas primeiras letras do Movimento (Escolha) feita pelo Player 2

        vencedor = -1
        if player1 == "PE" and player2 == "TE":
            vencedor = 0
        elif player1 == "TE" and player2 == "PE":
            vencedor = 1
        elif player1 == "PA" and player2 == "PE":
            vencedor = 0
        elif player1 == "PE" and player2 == "PA":
            vencedor = 1
        elif player1 == "TE" and player2 == "PA":
            vencedor = 0
        elif player1 == "PA" and player2 == "TE":
            vencedor = 1

        return vencedor # Resultado do vencedor da partida
