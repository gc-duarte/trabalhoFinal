import pygame

pygame.init()
running = True
FPS = 30

# Dimensões da janela

DIMENSÕES_TELA = pygame.display.Info()
LARGURA = DIMENSÕES_TELA.current_w
ALTURA = DIMENSÕES_TELA.current_h

# Caixas

TÍTULO_X = int(LARGURA*0.3054)
TÍTULO_TAMANHO_X = int(LARGURA*0.3895)
TÍTULO_Y = int(ALTURA*0.0662)
TÍTULO_TAMANHO_Y = int(ALTURA*0.1826)
TÍTULO_CENTRO = (TÍTULO_X+TÍTULO_TAMANHO_X // 2,TÍTULO_Y+TÍTULO_TAMANHO_Y // 2)
TÍTULO_POSIÇÃO = (TÍTULO_X,TÍTULO_Y,TÍTULO_TAMANHO_X,TÍTULO_TAMANHO_Y)

SELEÇÃO1_X = int(LARGURA*0.3724)
SELEÇÃO1_TAMANHO_X = int(LARGURA*0.2532)
SELEÇÃO1_Y = int(ALTURA*0.5780)
SELEÇÃO1_TAMANHO_Y = int(ALTURA*0.0857)
SELEÇÃO1_CENTRO = (SELEÇÃO1_X+SELEÇÃO1_TAMANHO_X // 2,SELEÇÃO1_Y+SELEÇÃO1_TAMANHO_Y // 2)
SELEÇÃO1_POSIÇÃO = (SELEÇÃO1_X,SELEÇÃO1_Y,SELEÇÃO1_TAMANHO_X,SELEÇÃO1_TAMANHO_Y)

SELEÇÃO2_Y = int(ALTURA*0.7202)
SELEÇÃO2_CENTRO = (SELEÇÃO1_X+SELEÇÃO1_TAMANHO_X // 2,SELEÇÃO2_Y+SELEÇÃO1_TAMANHO_Y // 2)
SELEÇÃO2_POSIÇÃO = (SELEÇÃO1_X,SELEÇÃO2_Y,SELEÇÃO1_TAMANHO_X,SELEÇÃO1_TAMANHO_Y)

SELEÇÃO3_Y = int(ALTURA*0.8536)
SELEÇÃO3_CENTRO = (SELEÇÃO1_X+SELEÇÃO1_TAMANHO_X // 2,SELEÇÃO3_Y+SELEÇÃO1_TAMANHO_Y // 2)
SELEÇÃO3_POSIÇÃO = (SELEÇÃO1_X,SELEÇÃO3_Y,SELEÇÃO1_TAMANHO_X,SELEÇÃO1_TAMANHO_Y)

# Imagens

FÍGURA_ESQUERDA_TAMANHO_X = int(LARGURA*0.1357)
FÍGURA_ESQUERDA_X = int(LARGURA*0.0947)
FÍGURA_ESQUERDA_TAMANHO_Y = int(ALTURA*0.2156)
FÍGURA_ESQUERDA_Y = int(ALTURA*0.6188)

FÍGURA_DIREITA_X = int(LARGURA*0.7831)
FÍGURA_DIREITA_TAMANHO_X = int(LARGURA*0.1097)

IMAGENS = {"Nave1":"Imagens/rocket_1.png","Nave2":"Imagens/rocket_2.png","Alien":"Imagens/ufo.png"}

# Texto

# 0.23 foi determinado experimentalmente
TAMANHO_TÍTULO = int((0.23*TÍTULO_TAMANHO_X+0.23*TÍTULO_TAMANHO_Y)/2)
TAMANHO_SELEÇÃO = int((0.23*SELEÇÃO1_TAMANHO_X+0.23*SELEÇÃO1_TAMANHO_Y)/2)
FONTE = "Fontes/Acme-Regular.ttf"
TEXTO = {"Título":"Nome_do_Jogo","Seleção1":"Jogar",
         "Seleção2":"Sair","Seleção3":"Campanha",
         "Seleção4":"Versus","Seleção5":"Voltar",
         "SeleçãoSkin":"Pressione Ação"}

# Mouse

MOUSE_POSIÇÃO = (0,0)

# Cores

CORES = {"Azul_Escuro":(14,14,38),"Branco":(255,255,255),
         "Vermelho":(255,0,0),"Verde":(0,255,0)}

# Modificadores globais

right = [False,False]
left = [False,False]
up = [False,False]
down = [False,False]
back = False

