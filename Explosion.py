import pygame
import datos


class Explosion(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(datos.abrir(datos.carpeta_explosiones, "0.png"))# carga imagen inicial
        self.rect = self.image.get_rect()
        self.tiempo = pygame.time.get_ticks()
        self.diametro = 0
        self.cont = 0
        self.pos = []
        self.explotar = False

    def iniciar(self, pos, diametro):
        self.diametro = diametro
        self.cont = 0
        self.rect.centerx = pos[0]
        self.rect.centery = pos[1]
        self.pos = pos
        self.explotar= True

    def update(self, ahora):
        if self.explotar and ahora - self.tiempo > 100 and self.cont < 9:
            self.image = pygame.transform.scale(
                pygame.image.load(datos.abrir(datos.carpeta_explosiones, f"{self.cont}.png")),  # carga imagenes explosion
                (self.diametro, self.diametro))
            self.rect = self.image.get_rect()
            self.rect.centerx = self.pos[0]
            self.rect.centery = self.pos[1]
            self.tiempo = pygame.time.get_ticks()
            self.cont += 1
