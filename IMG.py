import pygame

class Img(pygame.sprite.Sprite):

    def __init__(self,posx,posy,imagen):
        super().__init__()
        self.image = pygame.image.load(imagen)
        self.rect = self.image.get_rect()
        self.rect.centerx = posx
        self.rect.centery = posy
        self.width = self.rect.width
        self.height = self.rect.height

    #Cambiar imagen
    def camb(self,img):
        self.image = pygame.image.load(img)

    #Retornar variables del tamaño de la imagen
    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height
