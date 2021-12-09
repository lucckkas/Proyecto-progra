import pygame
import datos


class Checkbox:
    def __init__(self, pos):
        self.pos = pos
        self.activado = True
        self.letra = pygame.font.Font(None, 55)
        self.fondo = pygame.Surface((40, 40))
        self.image = pygame.Surface((30, 30))

    def dibujar(self, display):
        self.image.fill(datos.BLANCO)
        self.fondo.fill(datos.NEGRO)
        display.blit(self.fondo, self.pos)
        display.blit(self.image, [self.pos[0]+5, self.pos[1]+5])
        texto = self.letra.render("x", True, datos.NEGRO)
        if self.activado:
            display.blit(texto, [self.pos[0] + 9, self.pos[1]])

    def comprueba_click(self, posicion_mouse):
        if self.pos[0] <= posicion_mouse[0] <= self.pos[0]+40 \
                and self.pos[1] <= posicion_mouse[1] <= self.pos[1]+40:
            if self.activado:
                self.activado = False
            else:
                self.activado = True
