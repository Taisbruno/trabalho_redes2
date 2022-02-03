import pygame
from network_ import Network_ # Importando a Classe Network_
from pygame.locals import *
import pickle

pygame.font.init()
logo = pygame.image.load('logo.jpg') # Logo do grupo
altura = 700
largura = 700

janela = pygame.display.set_mode((largura, altura)) # Medidas do display da tela do client
pygame.display.set_caption("Jogo") # Titulo da janela do Client

class Botao:
    def __init__(self, texto, x, y, cor):
        self.texto = texto
        self.x = x
        self.y = y
        self.cor = cor
        self.largura = 150
        self.altura = 100

    def clique(self, posicao): 
        x1 = posicao[0]
        y1 = posicao[1]
        if self.x <= x1 <= self.x + self.largura and self.y <= y1 <= self.y + self.altura: # Diz se clicou no botão 
            return True
        else:
            return False

    def desenha(self, janela):
        pygame.draw.rect(janela, self.cor, (self.x, self.y, self.largura, self.altura))
        fonte = pygame.font.SysFont("calibri", 40) # Definindo a fonte e o tamanho das palavras do jogo
        texto = fonte.render(self.texto, 1, (230,230,250)) # Definindo a cor da fonte
        janela.blit(texto, (self.x + round(self.largura/2) - round(texto.get_width()/2), self.y + round(self.altura/2) - round(texto.get_height()/2))) # Faz com que o texto fique no centro do botão

def redesenhaTela(janela, jogo, player):
    janela.fill((224,255,255)) 
    if not(jogo.conectado()):# Caso só tenha uma pessoa conectada, manda a mensagem de que está esperando o outro jogador 
        fonte = pygame.font.SysFont("calibri", 65) 
        texto = fonte.render("Aguardando jogador...", 1, (0,0,0))
        janela.blit(texto, (largura/2 - texto.get_width()/2, altura/2 - texto.get_height()/2)) # Pro texto ficar no meio da tela
    else: # Caso os dois estejam conectados
        fonte = pygame.font.SysFont("calibri", 50) 
        texto = fonte.render("Você", 1, (0,0,0))
        janela.blit(texto, (110, 200))
        texto = fonte.render("Oponente", 1, (0,0,0))
        janela.blit(texto, (420, 200))
        mov1 = jogo.pegar_Mov(0)
        mov2 = jogo.pegar_Mov(1)
        if jogo.Mov_All(): # Se os dois jogadores já jogaram, continua o jogo 
            texto1 = fonte.render(mov1, 1, (0,0,0))
            texto2 = fonte.render(mov2, 1, (0,0,0))
        else: # Caso um jogador não tenha jogado, vai aparecer na tela pro seu adversário que ainda está escolhendo e pro adversário aparecerá que ele já escolheu
            if player == 0 and jogo.p1Mov:
                texto1 = fonte.render(mov1, 1, (0,0,0))
            elif jogo.p1Mov: # Jogador 1 jogou e o 2 não
                texto1 = fonte.render("Selecionado", 1, (0,0,0))
            else: 
                texto1 = fonte.render("Aguardando", 1, (0,0,0))

            if player == 1 and jogo.p2Mov: # Jogador 2 jogou, e o 1 não
                texto2 = fonte.render(mov2, 1, (0,0,0))
            elif jogo.p2Mov:
                texto2 = fonte.render("Selecionado", 1, (0,0,0))
            else:
                texto2 = fonte.render("Aguardando", 1, (0,0,0))

        if player == 1:
            janela.blit(texto2, (70, 350))
            janela.blit(texto1, (420, 350))
        else:
            janela.blit(texto1, (70, 350))
            janela.blit(texto2, (420, 350))

        for botao in botoes: # Escolha do botão
            botao.desenha(janela)

    pygame.display.update()

botoes = [Botao("Pedra", 75, 500, (123,104,238)), Botao("Tesoura", 275, 500, (255,99,71)), Botao("Papel", 475, 500, (0,139,139))] # Botão dos jogos para escolher sua opção

def main(): # Função principal
    relogio = pygame.time.Clock()
    go = True
    net = Network_() # Iniciando a classe Network_
    player = int(net.pegar_Pos()) # Pegando o número do Player (0 ou 1)
    print("Você é o jogador ", player) # Printa pro jogador qual o seu número

    while go:
        relogio.tick(60) # 60 segundos de tempo
        try:
            jogo = net.enviar("get") # Tentando pegar informações do jogo, comunicação com o servidor
        except:
            go = False
            print("Não encontrou jogo")
            break

        if jogo.Mov_All(): # Se ambos os jogadores fizeram seus movimentos
            redesenhaTela(janela, jogo, player) # Atualizar a tela com os movimentos feitos
            pygame.time.delay(500)
            try:
                jogo = net.enviar("reset") # Fala para o servidor resetar os movimentos pro próximo round
            except: 
                go = False
                print("Não encontrou jogo")
                break    
            fonte = pygame.font.SysFont("calibri", 80)
            if (jogo.vencedor() == 0 and player == 0) or (jogo.vencedor() == 1 and player == 1): # Verifica se o jogador venceu
                texto = fonte.render("Venceu!", 1, (60,179,113)) # Caso o jogador vença
            elif jogo.vencedor() == -1:
                texto = fonte.render("Empate!", 1, (255,215,0)) # Caso o jogador empate
            else:
                texto = fonte.render("Perdeu...", 1, (255,0,0)) # Caso o jogador perca

            janela.blit(texto, (largura/2 - texto.get_width()/2, altura/2 - texto.get_height()/2)) # Exibição, em cada Client, se venceu, perdeu, empatou...
            pygame.display.update()
            pygame.time.delay(2000)

        for event in pygame.event.get(): # Quando a pessoa clica no X da janela para sair do jogo
            if event.type == pygame.QUIT:
                go = False
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN: # Checagem de clique do mouse
                posicao = pygame.mouse.get_pos() # Pegar a posição do mouse
                for botao in botoes: # Faz algo a respeito sobre o click no determinado botão
                    if botao.clique(posicao) and jogo.conectado(): # Garante com que não se pode continuar jogando caso um dos jogadores não esteja online
                        if player == 0:
                            if not jogo.p1Mov:
                                net.enviar(botao.texto) # Movimento do jogador 0
                        else:
                            if not jogo.p2Mov:
                                net.enviar(botao.texto) # Movimento do jogador 1

        redesenhaTela(janela, jogo, player)

def tela_menu():
    go = True
    relogio = pygame.time.Clock() # Adiciona a função do relógio
    while go:
        relogio.tick(60)
        janela.fill((128, 128, 200))
        fonte = pygame.font.SysFont("calibri", 60)
        texto = fonte.render("Clique para jogar!", 1, (0,0,0))
        janela.blit(texto, (150,200))
        janela.blit(logo, (170,400))
        pygame.display.update()

        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: # Caso clique para sair do jogo
                pygame.quit()
                go = False
            if event.type == pygame.MOUSEBUTTONDOWN: # Caso clique em qualquer outra tecla 
                go = False
    main() # Chama a função main

while True:
    tela_menu()
        