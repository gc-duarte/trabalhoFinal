import pygame, sys
from Menus import *
from pygame import mixer
from enum import Enum

pygame.init()

clk = pygame.time.Clock()

TAMANHO_JANELA = (LARGURA,ALTURA)
screen = pygame.display.set_mode(TAMANHO_JANELA)
pygame.display.set_caption("Menu")

#mixer.music.load("Audio/One_Peice_15.mp3")
#mixer.music.play(-1)

##############################################################

class Direção(Enum):
    Direita = 0
    Esquerda = 1
    Cima = 2
    Baixo = 3

class Nave(pygame.sprite.Sprite):
    def __init__(self,screen,posição,tamanho,imagem,velocidade):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.velocidade = velocidade
        self.direção = Direção.Cima
        self.rodar = [False,False]
        self.tamanho = tamanho
        img = pygame.image.load(imagem)
        self.img_ = pygame.transform.scale(img,self.tamanho)
        # Atributo que pega a imagem com um certo tamanho
        self.rect = self.img_.get_rect()
        # Atributo que pega a o retângulo da imagem
        self.rect.center = posição

    def desenhar(self):
        if self.direção == Direção.Cima or self.direção == Direção.Baixo:  
          img = pygame.image.load(IMAGENS["Nave1"])
        elif self.direção == Direção.Direita or self.direção == Direção.Esquerda:  
          img = pygame.image.load(IMAGENS["Nave2"])

        self.img_ = pygame.transform.scale(img,self.tamanho)
        imagem = pygame.transform.flip(self.img_,self.rodar[0],self.rodar[1])
        self.screen.blit(imagem,self.rect)

    def mover(self,direita,esquerda,cima,baixo):
        dx,dy = 0,0

        if direita:
            dx = self.velocidade
            self.direção = Direção.Direita
            self.rodar[0] = False
            self.rodar[1] = False
        if esquerda:
            dx = -self.velocidade
            self.direção = Direção.Esquerda
            self.rodar[0] = True
            self.rodar[1] = False
        if cima:
            dy = -self.velocidade
            self.direção = Direção.Cima
            self.rodar[0] = False
            self.rodar[1] = False
        if baixo:
            dy = self.velocidade
            self.direção = Direção.Baixo
            self.rodar[0] = False
            self.rodar[1] = True
        else:
            pass

        self.rect.x += dx
        self.rect.y += dy 

class Jogador(Nave):
    def __init__(self,screen):
        super().__init__(screen,(SELEÇÃO1_X,SELEÇÃO1_Y),(FÍGURA_ESQUERDA_TAMANHO_X,FÍGURA_ESQUERDA_TAMANHO_Y),IMAGENS["Nave1"],15)

class Inimigo(Nave):
    def __init__(self,screen):
        super().__init__(screen,(TÍTULO_X,TÍTULO_Y),(FÍGURA_DIREITA_TAMANHO_X,FÍGURA_ESQUERDA_TAMANHO_Y),IMAGENS["Alien"],5)

player1 = Jogador(screen)
player2 = Jogador(screen)
right = [False,False]
left = [False,False]
up = [False,False]
down = [False,False]
alien = Inimigo(screen)
back = False

##############################################################

menu = Menu(screen)

while running:

  clk.tick(FPS)
  MOUSE_POSIÇÃO = pygame.mouse.get_pos()

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_ESCAPE:
        back = True
      if event.key == pygame.K_RIGHT:
        right[0] = True
      if event.key == pygame.K_LEFT:
        left[0] = True
      if event.key == pygame.K_UP:
        up[0] = True
      if event.key == pygame.K_DOWN:
        down[0] = True
      if event.key == pygame.K_d:
        right[1] = True
      if event.key == pygame.K_a:
        left[1] = True
      if event.key == pygame.K_w:
        up[1] = True
      if event.key == pygame.K_s:
        down[1] = True

    if event.type == pygame.KEYUP:
      if event.key == pygame.K_RIGHT:
        right[0] = False
      if event.key == pygame.K_LEFT:
        left[0] = False
      if event.key == pygame.K_UP:
        up[0] = False
      if event.key == pygame.K_DOWN:
        down[0] = False
      if event.key == pygame.K_d:
        right[1] = False
      if event.key == pygame.K_a:
        left[1] = False
      if event.key == pygame.K_w:
        up[1] = False
      if event.key == pygame.K_s:
        down[1] = False

    if event.type == pygame.MOUSEBUTTONDOWN:
      if event.button == 1: # botão esquerdo do mouse
        running = menu.mudar_menu(MOUSE_POSIÇÃO)

  screen.fill(CORES["Azul_Escuro"])
  menu.escolher_menu(MOUSE_POSIÇÃO)

  if menu.menu_atual == "Menu3":
    player1.desenhar()
    player1.mover(right[0],left[0],up[0],down[0])
    player2.desenhar()
    player2.mover(right[1],left[1],up[1],down[1])
    if back:
      menu.menu_atual = "Menu2"
      back = False

  pygame.display.flip()

pygame.quit()
sys.exit()
