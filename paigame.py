import pygame

# Importando uma função de uma biblioteca que ajusa a fechar o jogo
from sys import exit

# Inicia as coisas do pygame. Tem que fazer antes de tudo pra fazer funcionar as funções
pygame.init()

# Aqui a gente cria a janela do jogo. Usa uma tuple pra escolher largura e altura com set_mode()
janela = pygame.display.set_mode((800, 400))

# Nessa linha criamos o nome que aparece ali em cima da tela com .set_caption()
pygame.display.set_caption("Joguinho")

# O clock define qual vai ser o fps do jogo
clock = pygame.time.Clock()

# Essa variavel é só pra pintar o fundo da tela como o céu
cor_do_ceu = [51, 204, 204]

# Os objetos no pygame são chamados de surfaces.
# São tipo "placas" que a gente vai colocando em cima da tela.
chao = pygame.image.load("Jungle Asset Pack/Jungle Asset Pack/jungle tileset/chao.png").convert_alpha()
chao_grande = pygame.transform.scale(chao, (800, 50))
ceu = pygame.image.load("Jungle Asset Pack/Jungle Asset Pack/parallax background/plx-5.png").convert_alpha()
ceu_grande = pygame.transform.scale(ceu, (400, 400))
imagem_zumbi = pygame.image.load("Jungle Asset Pack/Jungle Asset Pack/Character/Zumbi.png").convert_alpha()

# Primeiro inimigo do jogo
zumbi = pygame.transform.scale(imagem_zumbi, (30, 50))
posicao_zumbi_x = 800
zumbi_retangulo = zumbi.get_rect(midbottom = (posicao_zumbi_x, 350))

# personagem.
# Aqui a gente cria a surface e depois um retangulo que usa pra posicionar e fazer outras coisas
imagem_personagem = pygame.image.load("Jungle Asset Pack/Jungle Asset Pack/Character/sprites/run.gif").convert_alpha()
personagem = pygame.transform.scale(imagem_personagem, (30, 50))
personagem_retangulo = personagem.get_rect(midbottom = (100, 350))

# Pra escrever precisamos criar uma fonte e depois colocar ela em uma surface pra escrever
fonte_teste = pygame.font.Font(None, 50)
surface_texto = fonte_teste.render("Joguinho", False, "yellow")

# aqui vai um loop que faz com que o jogo vá rodando sem a janela fechar
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    # Aqui vai ser desenhado tudo
    janela.fill(cor_do_ceu)
    janela.blit(ceu_grande, (0, 0))
    janela.blit(ceu_grande, (400, 0))
    janela.blit(chao_grande, (0, 350))
    janela.blit(surface_texto, (300, 50))
    janela.blit(zumbi, zumbi_retangulo)
    zumbi_retangulo.x -= 5
    if zumbi_retangulo.x <= -10:
        zumbi_retangulo.left = 800

    if personagem_retangulo.colliderect(zumbi_retangulo):
        print("bateu")

    janela.blit(personagem, personagem_retangulo)
    # atualizar a tela a cada frame com .update()
    pygame.display.update()
    clock.tick(60)