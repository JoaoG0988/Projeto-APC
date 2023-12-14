"""
Universidade de Brasilia
Instituto de Ciencias Exatas
Departamento de Ciencia da Computacao
Algoritmos e Programação de Computadores – 2/2023
Turma: Prof. Carla Castanho e Prof. Frank Ned
Aluno(a): < João Gabriel Machado Ferreira >
Matricula: < 232003607 >
Projeto Final - Parte 1
#TODO: Colocar uma descrição do projeto
Descricao: <  >
"""


import pygame
import sys
from funcoes import *

# Inicialização do Pygame
pygame.init()

# Definição de cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERMELHO = (255, 0, 0)

# Configurações da janela do menu do jogo
largura = 800
altura = 600
fonteprincial = pygame.font.SysFont("Bauhaus 93", 40)
fonte_instrucoes = pygame.font.Font(None, 30)
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Nome do Jogo")

# Função para desenhar o texto na tela
def desenhar_texto(texto, fonte, cor, x, y):
    texto_surface = fonte.render(texto, True, cor)
    texto_rect = texto_surface.get_rect()
    texto_rect.center = (x, y)
    tela.blit(texto_surface, texto_rect)


#Função que mostra as instruções do jogo
def instrucoes2():
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    menu2()

        tela.fill(BRANCO)      

        desenhar_texto("• Use as setas para cima e para baixo para mover a nave", fonte_instrucoes, PRETO, largura // 2, altura // 4)
        desenhar_texto('• Use a barra de espaço para atirar', fonte_instrucoes, PRETO, largura // 2, altura // 2.9)
        desenhar_texto('• Pegue os combustíveis para ganhar pontos e aumentar seu combustível', fonte_instrucoes, PRETO, largura // 2, altura // 2.3)
        desenhar_texto('• Evite os inimigos', fonte_instrucoes, PRETO, largura // 2, altura // 1.9)
        desenhar_texto('• Se você colidir com um inimigo ou ficar sem combustível, o jogo acaba', fonte_instrucoes, PRETO, largura // 2, altura // 1.6)
        desenhar_texto('Pressione"Espaço" para voltar ao menu do jogo', fonte_instrucoes, VERMELHO, largura // 2, altura // 1.2)


        pygame.display.flip()



def telainicial2():
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    menu2()

        tela.fill(PRETO)

        desenhar_texto("Bem vindo ao Baguncinha Espacial !!!", fonteprincial, VERMELHO, largura // 2, altura // 2.6)
        desenhar_texto('Pressione " Espaço " para começar ', fonteprincial, BRANCO, largura // 2, altura // 1.9)

        pygame.display.flip()



# Loop do menu do jogo
def menu2():
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                elif evento.key == pygame.K_1:
                    main() # Inicializa o jogo
                    print("Opção 1 selecionada - Jogar")
                elif evento.key == pygame.K_2:
                    print("Opção 2 selecionada - Configurações")
                elif evento.key == pygame.K_3:
                    print("Opção 3 selecionada - Ranking")
                elif evento.key == pygame.K_4:
                    instrucoes2() # Mostra as instruções
                elif evento.key == pygame.K_5:
                    pygame.quit()
                    sys.exit()

        # Limpar a tela
        tela.fill(PRETO)

        # Fonte para o título e menu
        fonte_titulo = pygame.font.SysFont("Bauhaus 93", 48)
        fonte_menu = pygame.font.Font(None, 36)

        # Desenhar o título
        desenhar_texto("Baguncinha Espacial", fonte_titulo, VERMELHO, largura // 2, altura // 4)

        # Desenhar opções do menu
        desenhar_texto("1. Jogar", fonte_menu, BRANCO, largura // 2, altura // 2 - 50)
        desenhar_texto("2. Configurações", fonte_menu, BRANCO, largura // 2, altura // 2)
        desenhar_texto("3. Ranking", fonte_menu, BRANCO, largura // 2, altura // 2 + 50)
        desenhar_texto("4. Instruções", fonte_menu, BRANCO, largura // 2, altura // 2 + 100)
        desenhar_texto("5. Sair", fonte_menu, BRANCO, largura // 2, altura // 2 + 150)

        # Atualizar a tela
        pygame.display.flip()




# Iniciar a tela incial do jogo
telainicial2()
