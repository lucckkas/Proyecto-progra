import pygame
import datos


class Triangulo(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load(datos.abrir(datos.carpeta_tanke, "turno.png"))  # carga imagen inicial
        self.rect = self.image.get_rect()
        self.tiempo = pygame.time.get_ticks()
        self.cont = 0
        self.sube = False
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def dibujar(self, pantalla, ahora):
        pantalla.blit(self.image, [self.rect.x, self.rect.y + self.cont - 35])
        if ahora - self.tiempo > 20:
            # cambia imagenes
            self.image = self.image = pygame.image.load(datos.abrir(
                datos.carpeta_tanke, "turno.png"))
            self.tiempo = pygame.time.get_ticks()

            if self.sube:
                self.cont -= 1
            else:
                self.cont += 1

            if self.cont <= -5:
                self.sube = False
            if self.cont >= 5:
                self.sube = True

    def mover(self, pos):
        self.rect.center = pos
