from config import*
from clases import Nave #[1]
import pygame ,sys

pygame.init()
relog=pygame.time.Clock()

screen=pygame.display.set_mode(SIZE)
pygame.display.set_caption("Nuevo proyecto")
fondo=pygame.image.load("./images/fondo.jpg").convert()
#llamar a la funcion constructora [1]
nave= Nave("./images/nae.png",SIZE_SHIP,(screen.get_width()//2,screen.get_height() - 20 ))


fondo=pygame.transform.scale(fondo,(WIDTH,HEIGHT))
while True:
    relog.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            nave.rect.center = pygame.mouse.get_pos()
        elif event.type == pygame.KEYDOWN:
            if event.key== pygame.K_LEFT:
                nave.velocidad_x = -SPEED_SHIP
            if event.key== pygame.K_RIGHT:
                nave.velocidad_x = SPEED_SHIP

    nave.update()
  

    
    screen.blit(fondo,(0,0))
    screen.blit(nave.image,nave.rect)
    pygame.display.flip()

