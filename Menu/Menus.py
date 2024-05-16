import pygame
from config import *
from Naves import *

pygame.init()

class Menu(pygame.sprite.Sprite):

  def __init__(self,screen)->None:
    self.menu_atual = "Menu1"
    self.screen = screen

  def desenhar_texto(self,tamanho_fonte:int,seleção:str,cor:str,centro:tuple,posição:tuple)->None:
    fonte = pygame.font.Font("Fontes/Acme-Regular.ttf",tamanho_fonte)
    texto = fonte.render(TEXTO[seleção],True,CORES[cor])
    texto_rect = texto.get_rect(center=centro)
    pygame.draw.rect(self.screen,CORES[cor],posição,2)
    self.screen.blit(texto,texto_rect)

  def mudar_menu(self,MOUSE_POSIÇÃO:tuple)->bool:
    if self.menu_atual == "Menu1":
      if (MOUSE_POSIÇÃO[1] >= SELEÇÃO1_Y and MOUSE_POSIÇÃO[1] <= (SELEÇÃO1_Y+SELEÇÃO1_TAMANHO_Y)) and (MOUSE_POSIÇÃO[0] >= SELEÇÃO1_X and MOUSE_POSIÇÃO[0] <= (SELEÇÃO1_X+SELEÇÃO1_TAMANHO_X)):
        self.menu_atual = "Menu2"
        return True # Jogar 
      elif (MOUSE_POSIÇÃO[1] >= SELEÇÃO2_Y and MOUSE_POSIÇÃO[1] <= (SELEÇÃO2_Y+SELEÇÃO1_TAMANHO_Y)) and (MOUSE_POSIÇÃO[0] >= SELEÇÃO1_X and MOUSE_POSIÇÃO[0] <= (SELEÇÃO1_X+SELEÇÃO1_TAMANHO_X)):
        # Sair
        return False
      else:
        return True
    elif self.menu_atual == "Menu2":
      if (MOUSE_POSIÇÃO[1] >= SELEÇÃO3_Y and MOUSE_POSIÇÃO[1] <= (SELEÇÃO3_Y+SELEÇÃO1_TAMANHO_Y)) and (MOUSE_POSIÇÃO[0] >= SELEÇÃO1_X and MOUSE_POSIÇÃO[0] <= (SELEÇÃO1_X+SELEÇÃO1_TAMANHO_X)):
        self.menu_atual = "Menu1" # Voltar
        return True
      elif (MOUSE_POSIÇÃO[1] >= SELEÇÃO1_Y and MOUSE_POSIÇÃO[1] <= (SELEÇÃO1_Y+SELEÇÃO1_TAMANHO_Y)) and (MOUSE_POSIÇÃO[0] >= SELEÇÃO1_X and MOUSE_POSIÇÃO[0] <= (SELEÇÃO1_X+SELEÇÃO1_TAMANHO_X)):
        # Campanha
        return True
      elif (MOUSE_POSIÇÃO[1] >= SELEÇÃO2_Y and MOUSE_POSIÇÃO[1] <= (SELEÇÃO2_Y+SELEÇÃO1_TAMANHO_Y)) and (MOUSE_POSIÇÃO[0] >= SELEÇÃO1_X and MOUSE_POSIÇÃO[0] <= (SELEÇÃO1_X+SELEÇÃO1_TAMANHO_X)):
        # Versus
        self.menu_atual = "Menu3"
        return True  
      else:
        return True
    else:
      return True

  def escolher_menu(self,MOUSE_POSIÇÃO:tuple)->None:
    self.desenhar_texto(TAMANHO_TÍTULO,"Título","Vermelho",TÍTULO_CENTRO,TÍTULO_POSIÇÃO)
    match self.menu_atual:
      case "Menu1":
        self.desenhar_texto(TAMANHO_SELEÇÃO,"Seleção1","Branco",SELEÇÃO1_CENTRO,SELEÇÃO1_POSIÇÃO)
        self.desenhar_texto(TAMANHO_SELEÇÃO,"Seleção2","Branco",SELEÇÃO2_CENTRO,SELEÇÃO2_POSIÇÃO)
      case "Menu2":
        self.desenhar_texto(TAMANHO_SELEÇÃO,"Seleção3","Branco",SELEÇÃO1_CENTRO,SELEÇÃO1_POSIÇÃO)
        self.desenhar_texto(TAMANHO_SELEÇÃO,"Seleção4","Branco",SELEÇÃO2_CENTRO,SELEÇÃO2_POSIÇÃO)
        self.desenhar_texto(TAMANHO_SELEÇÃO,"Seleção5","Branco",SELEÇÃO3_CENTRO,SELEÇÃO3_POSIÇÃO)
        if (MOUSE_POSIÇÃO[1] >= SELEÇÃO2_Y and MOUSE_POSIÇÃO[1] <= (SELEÇÃO2_Y+SELEÇÃO1_TAMANHO_Y)) and (MOUSE_POSIÇÃO[0] >= SELEÇÃO1_X and MOUSE_POSIÇÃO[0] <= (SELEÇÃO1_X+SELEÇÃO1_TAMANHO_X)):
          imagem1 = pygame.image.load(IMAGENS["Nave1"])
          imagem1 = pygame.transform.scale(imagem1,(FÍGURA_ESQUERDA_TAMANHO_X,FÍGURA_ESQUERDA_TAMANHO_Y))
          imagem1_rect = (FÍGURA_ESQUERDA_X,FÍGURA_ESQUERDA_Y)
          self.screen.blit(imagem1,imagem1_rect)
          imagem2 = pygame.image.load(IMAGENS["Nave1"])
          imagem2 = pygame.transform.scale(imagem2,(FÍGURA_ESQUERDA_TAMANHO_X,FÍGURA_ESQUERDA_TAMANHO_Y))
          imagem2_rect = (FÍGURA_DIREITA_X,FÍGURA_ESQUERDA_Y)
          self.screen.blit(imagem2,imagem2_rect)
          # Versus
        elif (MOUSE_POSIÇÃO[1] >= SELEÇÃO1_Y and MOUSE_POSIÇÃO[1] <= (SELEÇÃO1_Y+SELEÇÃO1_TAMANHO_Y)) and (MOUSE_POSIÇÃO[0] >= SELEÇÃO1_X and MOUSE_POSIÇÃO[0] <= (SELEÇÃO1_X+SELEÇÃO1_TAMANHO_X)):
          imagem1 = pygame.image.load(IMAGENS["Nave1"])
          imagem1 = pygame.transform.scale(imagem1,(FÍGURA_ESQUERDA_TAMANHO_X,FÍGURA_ESQUERDA_TAMANHO_Y))
          imagem1_rect = (FÍGURA_ESQUERDA_X,FÍGURA_ESQUERDA_Y)
          self.screen.blit(imagem1,imagem1_rect)
          imagem2 = pygame.image.load(IMAGENS["Alien"])
          imagem2 = pygame.transform.scale(imagem2,(FÍGURA_DIREITA_TAMANHO_X,FÍGURA_ESQUERDA_TAMANHO_Y))
          imagem2_rect = (FÍGURA_DIREITA_X,FÍGURA_ESQUERDA_Y)
          self.screen.blit(imagem2,imagem2_rect)
          # Campanha
      case _:
        pass
