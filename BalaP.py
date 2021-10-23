from Bala import Bala
import pygame
import datos
class BalaP(Bala):
    def __init__(self):
        super().__init__()
        self.tipo_bala="perforante"
        self.image = pygame.image.load(datos.abrir(datos.carpeta_balas, f"{self.tipo_bala}.png"))
        self.rect = self.image.get_rect()
        self.tipo = f"{self.tipo_bala}.png"
        self.dagno = datos.dagno_perforante
        self.tam_explocion = datos.tam_exp_perforante
        self.imagen_original = pygame.image.load(datos.abrir(datos.carpeta_balas, f"{self.tipo_bala}.png"))
    def get_diametro(self):
        return self.dagno*4-40
