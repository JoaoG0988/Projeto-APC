import pygame
import sys

# Inicialização do Pygame
pygame.init()

# Configurações da tela
largura_tela2 = 800
altura_tela2 = 600
tela = pygame.display.set_mode((largura_tela2, altura_tela2))
pygame.display.set_caption('Game Over')

# Cores
preto = (0, 0, 0)
branco = (255, 255, 255)
vermelho = (255, 0, 0)

# Fonte para o texto
fonte = pygame.font.Font(None, 36)

def desenhar_texto(texto, fonte, cor, x, y):
    texto_surface = fonte.render(texto, True, cor)
    texto_rect = texto_surface.get_rect()
    texto_rect.center = (x, y)
    tela.blit(texto_surface, texto_rect)

def game_over():
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


        # Desenha a tela de Game Over
        tela.fill(branco)
        desenhar_texto("• Use as setas para cima e para baixo para mover a nave", fonte, preto, largura_tela2 // 1, altura_tela2 // 1)
        '''
        texto = fonte.render('Game Over', True, vermelho)
        tela.blit(texto, (largura_tela // 2 - texto.get_width() // 2, altura_tela // 2 - texto.get_height() // 2))
        '''
        pygame.display.update()




