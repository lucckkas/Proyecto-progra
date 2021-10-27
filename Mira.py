import pygame


class Mira(pygame.sprite.Sprite):
    def __init__(self, posX, posY, imagen):
        super().__init__()
        self.image = pygame.image.load(imagen)
        self.image.set_colorkey([255, 255, 255])
        self.rect = self.image.get_rect()
        self.rect.centerx = posX
        self.rect.centery = posY
        self.widht = self.image.get_width()
        self.heigh = self.image.get_height()
        # copia del la imagen para poder rotar
        self.imagenR = pygame.image.load(imagen)

    # rotar dependiendo del angulo
    def rotar(self, surface, angulo):
        rotada_img = pygame.transform.rotozoom(surface, angulo, 1)
        rotada_pos = rotada_img.get_rect(center=(self.rect.centerx, self.rect.centery))
        return rotada_img, rotada_pos
    # retornar valores del tamaño de la imagen

    def getWidht(self):
        return self.widht

    def getHeigh(self):
        return self.heigh
