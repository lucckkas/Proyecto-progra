import pygame
import datos


class Boton(pygame.sprite.Sprite):
    def __init__(self, imagen, posicion, tamagno):
        super().__init__()
        imagen = datos.abrir(datos.carpeta_boton, imagen)
        self.image = pygame.transform.scale(pygame.image.load(imagen), tamagno)
        self.rect = self.image.get_rect(center=posicion)
        self.rect.center = posicion
        self.tamagno = tamagno

    def click(self, posicion_mouse):
        if (self.rect.centerx-(self.tamagno[0]/2) <= posicion_mouse[0] <= self.rect.centerx+(self.tamagno[0]/2) and
                self.rect.centery-(self.tamagno[1]/2) <= posicion_mouse[1] <= self.rect.centery+(self.tamagno[1]/2)):
            return True
        return False

    def dibujar(self, pantalla):
        pantalla.blit(self.image, (self.rect.x, self.rect.y))
