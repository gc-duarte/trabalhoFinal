from enum import Enum
from config import *

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
        self.direção = Direção.Direita
        self.rodar = [True,False]
        img = pygame.image.load(imagem)
        self.img_ = pygame.transform.scale(img,tamanho)
        # Atributo que pega a imagem com um certo tamanho
        self.rect = self.img_.get_rect()
        # Atributo que pega a o retângulo da imagem
        self.rect.center = posição

    def desenhar(self):
        imagem = pygame.transform.flip(self.img_,self.rodar[0],self.rodar[1])
        self.screen.blit(imagem,self.rect)

    def mover(self,direita,esquerda,cima,baixo):
        dx,dy = 0,0

        if direita:
            dx = self.velocidade
            self.rodar[0] = False
            self.rodar[1] = False
        if esquerda:
            dx = -self.velocidade
            self.rodar[0] = True
            self.rodar[1] = False
        if cima:
            dy = -self.velocidade
            self.rodar[0] = False
            self.rodar[1] = True
        if baixo:
            dy = self.velocidade
            self.rodar[0] = True
            self.rodar[1] = True
        else:
            pass

        self.rect.x += dx
        self.rect.y += dy 

class Jogador(Nave):
    def __init__(self,screen):
        super().__init__(screen,(SELEÇÃO1_X,SELEÇÃO1_Y),(FÍGURA_ESQUERDA_TAMANHO_X,FÍGURA_ESQUERDA_TAMANHO_Y),"Imagens/rocket_red.png",15)

class Inimigo(Nave):
    def __init__(self,screen):
        super().__init__(screen,(TÍTULO_X,TÍTULO_Y),(FÍGURA_DIREITA_TAMANHO_X,FÍGURA_ESQUERDA_TAMANHO_Y),"Imagens/ufo.png",5)
