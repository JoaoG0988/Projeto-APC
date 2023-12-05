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

#Importação das bibliotecas
import pygame
import random
import sys
def menu():
    print('Escolha uma opção:')
    print('1 - Jogar')
    print('2 - Configurações')
    print('3 - Ranking')
    print('4 - Instruções')
    print('5 - Sair')
    escolha = int(input('Escolha uma opção : '))
    match escolha:
        case 1: main() # Inicia a janela do jogo.
        case 2: configs()
        case 3: ranking()
        case 4: instrucoes()
        case 5: sair()
        case _: # Caso o número digitado não for válido, mostrará a mensagem de erro e chamará o menu até que um número válido seja digitado
            print('Por favor, digite uma opção válida.')
            menu()

def telainicial():
    print(' ')
    print('Boas vindas ao ESTRAGAWARS !!! ')
    print(' ')
    print('+='* 30)
    print(' ')
    print('Selecione qualquer tecla, em seguida aperte "Enter" para começar !')
    print(' ')
    input()
    menu()
    



def configs():
    print('Ainda não disponível')

def ranking():
    print('Ainda não disponível')

def instrucoes():
    print(" ")
    print('Instruções do jogo:')
    print(" ")
    print('+='* 35)
    print(" ")
    print(' • Use as setas para cima e para baixo para mover a nave')
    print(' • Use a barra de espaço para atirar')
    print(' • Pegue os combustíveis para ganhar pontos e aumentar seu combustível')
    print(' • Evite os inimigos')
    print(' • Se você colidir com um inimigo ou ficar sem combustível, o jogo acaba')
    print(' ')
    print('+='* 35)
    print(' ')
    print('Selecione qualquer tecla, em seguida aperte "Enter" para voltar ao menu do jogo')
    input()
    menu()

def sair():
    print('Obrigado por jogar!')
    sys.exit()

def main():
    pygame.init()

    # Algumas variaveis do jogo
    tamanho = 10
    largura_tela, altura_tela = 135*tamanho,10*tamanho
    probX = 12
    probF = 10
    velo_player = 5
    velo_inimigo = 6
    velo_tiro = 10
    combus_quant = 1
    combust_tiro = 3
    jogador_largura = 10
    jogador_altura = 10
    tiro_largura = 10
    tiro_altura = 10
    inimigo_largura, inimigo_altura = 10, 10
    fps = 20

    # Cores dos elementos presentes no jogo
    branco = (255, 255, 255)
    preto = (0, 0, 0)
    vermelho = (255, 0, 0)
    azul = (0,100,200)
    verde = (0,255,0)
    verde_escuro = (0,100,0)
    #amarelo = (255, 255, 0)


    # Criação da tela
    tela = pygame.display.set_mode((largura_tela, altura_tela))
    pygame.display.set_caption("ESTRAGAWARS")

    # Elementos do jogo
    jogador = pygame.Rect(0, 42, tamanho,tamanho)
    combust = [pygame.Rect(random.randint(1400, 2000),random.randint(0, 90), inimigo_largura, inimigo_altura) for _ in range(probF)]
    inimigos = [pygame.Rect(random.randint(1400, 2000),random.randint(0, 80), inimigo_largura, inimigo_altura) for _ in range(probX)]
    tiro = []
    tiro_status = False  

    # Algumas variaveis do jogo
    morte1 = 'Seu combustível esgotou' 
    morte2 = 'Você foi tingido pelo inimigo'
    score = 0
    combustivel = 400  # Quantidade inicial de combustivel
    font = pygame.font.Font(None, 15)
    font2 = pygame.font.Font(None, 20)
    run = True


    #Tela de game over.
    def game_over1():
        texto_gameover = font2.render("Game Over", True, vermelho)
        texto_score = font2.render(f"Pontuação final: {score}", True, branco)
        texto_motivo = font2.render(f'{morte1}', True, branco)
        tela.blit(texto_gameover, (largura_tela // 2 - texto_gameover.get_width() // 2, altura_tela // 2 - texto_gameover.get_height() // 1))
        tela.blit(texto_score, (largura_tela // 2 - texto_score.get_width() // 2, altura_tela // 2 + 10))
        tela.blit(texto_motivo, (largura_tela // 2 - texto_motivo.get_width() // 2, altura_tela // 20))

        pygame.display.update()
        pygame.time.delay(6000) # A tela de game over aparece por 6 segundos,fecha a janela do jogo e retorna ao menu.
        pygame.display.quit()
        menu()
        

    def game_over2():
        texto_gameover = font2.render("Game Over", True, vermelho)
        texto_score = font2.render(f"Pontuação final: {score}", True, branco)
        texto_motivo = font2.render(f'{morte2}', True, branco)
        tela.blit(texto_gameover, (largura_tela // 2 - texto_gameover.get_width() // 2, altura_tela // 2 - texto_gameover.get_height() // 1))
        tela.blit(texto_score, (largura_tela // 2 - texto_score.get_width() // 2, altura_tela // 2 + 10))
        tela.blit(texto_motivo, (largura_tela // 2 - texto_motivo.get_width() // 2, altura_tela // 20))
        
        pygame.display.update()
        pygame.time.delay(6000) # A tela de game over aparece por 6 segundos,fecha a janela do jogo e retorna ao menu.
        pygame.display.quit()
        menu()


    # Função para mostrar os status dos pontos e quantidade de combustivel
    def pontuação():
        pont_score = font.render(f"Pontos: {score}", True, branco)
        combust_score = font.render(f"Combustível: {combustivel:.0f}", True, branco)
        tela.blit(pont_score, (5, 5))
        tela.blit(combust_score, (largura_tela - combust_score.get_width() - 5, 5))

    clock = pygame.time.Clock()
    

    # Aqui é onde começa o loop do jogo
    while run:
        tela.fill(preto)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            # Movimentação do jogador.
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if jogador.y > 3:
                        jogador.y -= velo_player
                        combustivel -= 2

                elif event.key == pygame.K_DOWN:
                    if jogador.y < 87:
                        jogador.y += velo_player
                        combustivel -= 2
                        
                elif event.key == pygame.K_SPACE and len(tiro) < 9999999999:
                    if combustivel >= combust_tiro:
                        tiros = pygame.Rect(jogador.x + jogador.height // 2 - 2, jogador.y, tiro_largura, tiro_altura)
                        tiro.append(tiros)
                        tiro_status = True
                        combustivel -= combust_tiro

        # Movimento do tiro da nave.
        for tiros1 in tiro:
            tiros1.x += velo_tiro
            if tiros1.x <= 0:
                tiros1.remove(tiros1)

    
        # Movimento do inimigo.
        for inimigo1 in inimigos:
            pygame.draw.rect(tela,vermelho, inimigo1)
            inimigo1.x -= velo_inimigo

            #Morte do jogador se ele for atingido por um inimigo
            if inimigo1.colliderect(jogador):
                tela.fill(preto)
                game_over2()
                

            if inimigo1.x < -20:
                inimigo1.x = random.randint(largura_tela, largura_tela + inimigo_largura)
                inimigo1.y = random.randint(0, altura_tela - inimigo_altura)

            #Eliminação do inimigo ao ser atingido( se o inimigo for atingido,a pontuação é incrementada em 50).
            for tiros1 in tiro:
                if tiros1.colliderect(inimigo1):
                    tiro.remove(tiros1)
                    score += 50 
                    inimigo1.x = 0
                    inimigo1.y = random.randint(100, largura_tela - 100)
            
                                

        #Movimento do combustivel e colisão com os tiros
        for combust1 in combust:
            pygame.draw.rect(tela,azul, combust1)
            combust1.x -= velo_inimigo

            if combust1.x < -20:
                combust1.x = random.randint(largura_tela, largura_tela + inimigo_largura)
                combust1.y = random.randint(0, altura_tela - inimigo_altura)       


            #Se o combustivel encostar no jogador,o combustível é incrementado em 40
            for combust1 in combust:
                if combust1.colliderect(jogador):
                    combust1.x = 0
                    combust1.y = random.randint(100, largura_tela - 100)
                    combustivel += 40

                for tiros1 in tiro:
                    if tiros1.colliderect(combust1):
                        tiro.remove(tiros1)
                        combust1.x = 0
                        combust1.y = random.randint(100, largura_tela - 100)
                        
                    

                        
                
            
                    
    
    
        # Quantidade de combustivel
        combustivel -= 0.1
        if combustivel <= 0:
            tela.fill(preto)
            game_over1()      # Game over se o combustivel acabar
             


        # Para mostrar a nave,tiros,pontuação,combustivel
        pygame.draw.rect(tela, verde, jogador)
        for tiros1 in tiro:
            pygame.draw.rect(tela, verde_escuro, tiros1)
        pontuação()

        pygame.display.update()
        clock.tick(fps)  #Controlar a taxa de atualização da tela

    #pygame.quit()
    #sys.exit()

telainicial()