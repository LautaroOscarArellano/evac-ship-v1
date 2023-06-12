from config import*
from clases import Nave #[1]
from clases import Asteroide
import pygame ,sys, random

def generar_asteroides(grupo_asteroides , grupo_sprites , cantidad : int):
    if len(grupo_asteroides) == 0:
        for i in range(cantidad):
            posicion=(random.randrange(40,WIDTH-20)),random.randrange(-500,HEIGHT // 2)
            asteroides=Asteroide("./images/raptor.png", SIZE_ASTEROIDE,posicion,SPEED_ASTEROIDE )
            grupo_asteroides.add(asteroides)
            grupo_sprites.add(asteroides)


pygame.init()
relog=pygame.time.Clock()

screen=pygame.display.set_mode(SIZE)
pygame.display.set_caption("Nuevo proyecto")
fondo=pygame.image.load("./images/fondo.jpg").convert()

sprites=pygame.sprite.Group()
asteroides=pygame.sprite.Group()
lasers=pygame.sprite.Group()

#llamar a la funcion constructora [1]
nave= Nave("./images/raptor.png",SIZE_SHIP,(screen.get_width()//2,screen.get_height() - 20 ))
sprites.add(nave)#agregamos la nave al grupo de los sprites 
generar_asteroides(asteroides,sprites,MAX_ASTEROIDES)

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

            if event.key== pygame.K_UP:
                nave.velocidad_y = -SPEED_SHIP
            if event.key== pygame.K_DOWN:
                nave.velocidad_y = SPEED_SHIP
                
        elif event.type == pygame.KEYUP:
            if event.key== pygame.K_UP:
                nave.velocidad_x = 0
            if event.key== pygame.K_DOWN:
                 nave.velocidad_x = 0


        pygame.sprite.collide_rect()

    lista=generar_asteroides(asteroides,sprites,MAX_ASTEROIDES)
    sprites.update()

    if nave.rect.left <=0:
        nave.rect.left = 0
    elif nave.rect.right >= WIDTH:
        nave.rect.right = WIDTH

    if nave.rect.top <=0:
        nave.rect.top = 0
    elif nave.rect.bottom >= HEIGHT:
        nave.rect.bottom = HEIGHT

    for asteroide in asteroides:
        if asteroide.rect.bottom >= HEIGHT:
            asteroide.kill()

    pygame.sprite.spritecollide(nave , asteroide , True)
          
        # if event.key==pygame.K_UP:
        #     pass
        # if event.key==pygame.K_DOWN:
        #     pass   

 
    screen.blit(fondo,(0,0))
    sprites.draw(screen)
    #screen.blit(nave.image,nave.rect)
    pygame.display.flip()


#Notaciones
"""

sonido = pygame.mixed.sound/laser.mp3



"""