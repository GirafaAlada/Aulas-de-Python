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

# Os objetos no pygame são chamados de surfaces
chao = pygame.image.load("Jungle Asset Pack/Jungle Asset Pack/jungle tileset/chao.png")
chao_grande = pygame.transform.scale(chao, (800, 50))
ceu = pygame.image.load("Jungle Asset Pack/Jungle Asset Pack/parallax background/plx-5.png")
ceu_grande = pygame.transform.scale(ceu, (400, 400))

# Essa variavel é só pra pintar o fundo da tela como o céu
cor_do_ceu = [51, 204, 204]


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
    # atualizar a tela a cada frame com .update()
    pygame.display.update()
    clock.tick(60)