import pygame
import datos


class Checkbox:
    def __init__(self, pos):
        self.pos = pos
        self.activado = True
        self.image = pygame.Surface((40, 40))

    def dibujar(self, display):
        if self.activado:
            self.image.fill(datos.VERDE)
        else:
            self.image.fill(datos.ROJO)
        display.blit(self.image, self.pos)

    def comprueba_click(self, posicion_mouse):
        if self.pos[0] <= posicion_mouse[0] <= self.pos[0]+40 \
                and self.pos[1] <= posicion_mouse[1] <= self.pos[1]+40:
            if self.activado:
                self.activado = False
            else:
                self.activado = True
