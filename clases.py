from typing import Any
import pygame

"""
Siempre un sprite tiene que tener una imagen y un self fact[gereda]
definir un evento update(self)
"""
class Nave(pygame.sprite.Sprite):
    def __init__(self ,path_imagen:str , size:tuple , mid_bottom:tuple):
        super().__init__()#"""Llamar al  constructor del padre
        self.image=pygame.image.load(path_imagen).convert_alpha()
        self.image=pygame.transform.scale(self.image ,size)

        self.rect = self.image.get_rect() #guardar el rect de la imagen
        self.rect.midbottom=mid_bottom

        self.velocidad_x=0
        self.velocidad_y=0

    def update(self):
        self.rect.x += self.velocidad_x