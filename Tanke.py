# -*- coding: utf-8 -*-
#tanque estandar
import Tank
from IMG import Img
from Bala import Bala
from Mira import Mira
import datos
import math
import pygame
from Explosion import Explosion
from Bala60 import Bala60
from BalaP import  BalaP
from Bala105 import Bala105

#transformar de grados a radianes
def trans_ang_rad(ang):
    return ang * math.pi / 180
class Tanke(Tank.Tank):
    def __init__(self, Imagen, posX, posY,miraImg):
        super().__init__(Imagen, posX, posY,miraImg)
        self.image = pygame.image.load(Imagen)
        # borrar fonndo imagen
        self.image.set_colorkey(datos.BLANCO)
        self.rect = self.image.get_rect()
        self.rect.centerx = posX
        self.rect.centery = posY
        self.inventario1 = 3
        self.inventario2 = 10
        self.inventario3 = 3
        self.life = 100
        self.bala = Bala60()
        self.explosion = Explosion()
        self.sprites.add(self.explosion)




################################################

