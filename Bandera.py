import pygame
import datos
from math import fabs


class Bandera(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load(datos.abrir(datos.carpeta_bandera, "0.png"))  # carga imagen inicial
        self.rect = self.image.get_rect()
        self.tiempo = pygame.time.get_ticks()
        self.cont = 1
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.direccion = ""

    def dibujar(self, pantalla, ahora):
        if datos.viento < 0:
            self.direccion = "i"
        else:
            self.direccion = "d"

        pantalla.blit(self.image, (self.rect.x, self.rect.y))
        if ahora - self.tiempo > 100-fabs(datos.viento)*7 and self.cont < 7 and datos.viento != 0:
            # cambia imagenes
            self.image = self.image = pygame.image.load(datos.abrir(
                datos.carpeta_bandera, f"{self.cont}{self.direccion}.png"))
            self.tiempo = pygame.time.get_ticks()
            self.cont += 1
            if self.cont == 7:
                self.cont = 1
        elif datos.viento == 0:
            self.image = pygame.image.load(datos.abrir(datos.carpeta_bandera, "0.png"))
