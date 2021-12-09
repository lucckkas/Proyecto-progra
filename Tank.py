import math
import pygame
import datos
from Bala import Bala
from Explosion import Explosion
from IMG import Img
from Mira import Mira

TAM_MAPA = datos.tamagno_mapa[0]


# transformar de grados a radianes
def trans_ang_rad(ang):
    return ang * math.pi / 180


class Tank(pygame.sprite.Sprite):
    def __init__(self, imagen, posX, posY, miraImg):
        super().__init__()
        self.image = pygame.image.load(imagen)
        # borrar fonndo imagen
        self.rect = self.image.get_rect()
        self.rect.centerx = posX
        self.rect.bottom = posY + 10  # sumo 10 pixeles a los tankes para evitar que se apoyen en colinas super enanas
        self.height = self.image.get_height()
        self.width = self.image.get_width()
        self.potencia = 40
        self.angle = 0
        self.disparable = True
        self.inventario1 = datos.balas_60mm
        self.inventario2 = datos.balas_perforantes
        self.inventario3 = datos.balas_105mm
        self.inventarioF = datos.balas_60mm
        self.life = 100
        self.cambia_angulo = 0
        self.cambia_potencia = 0
        self.wLife = 200
        self.bala = Bala()
        self.explosion = Explosion()
        self.kills = 0
        # crear la mira en su posicion correspondiente al centro en x y en su posicion y correspondiente
        self.mira = Mira(self.rect.x + self.width / 2, self.rect.y + self.height / 4.5, miraImg)
        # crear grupo donde estaran los sprites a dibujar
        self.sprites = pygame.sprite.Group()
        self.sprites.add(self)
        self.sprites.add(self.mira)
        self.sprites.add(self.explosion)
        self.corona = Img(0, 0, datos.abrir(datos.carpeta_tanke, "Corona.png"))



    #def dibujar(self, pantalla):






    def disparar(self):
        # disparar la bala dependiendo desde la punta de la mira
        if self.disparable and self.vivo():
            # agregar la bala a los sprites visibles
            self.sprites.add(self.bala)
            if self.bala.tipo == "60mm.png" and self.inventario1 > 0:
                self.inventario1 += -1
            elif self.bala.tipo == "perforante.png" and self.inventario2 > 0:
                self.inventario2 += -1
            elif self.bala.tipo == "105mm.png" and self.inventario3 > 0:
                self.inventario3 += -1

            # posicionar la bala en la mira usadando un offset en X y en Y
            self.bala.disparar(self.angle, self.potencia, self.mira.rect.centerx + self.offsetx(),
                               self.mira.rect.centery - self.offsety())

    def dispararIA(self, angulo_potencia):
        if self.inventarioF == 0:
            if self.inventario1 > 0:
                self.bala = Bala()
                self.inventarioF = self.inventario1

            elif self.inventario2 > 0:
                self.bala = Bala("perforante")
                self.inventarioF = self.inventario2

            elif self.inventario3 > 0:
                self.bala = Bala("105mm")
                self.inventarioF = self.inventario3

            if self.inventarioF == 0:
                self.disparable = False
            else:
                self.disparable = True

        if self.inventarioF != 0:
            self.angle = angulo_potencia[0]
            self.potencia = angulo_potencia[1]
            self.disparar()

    # Retornar valores del tanque
    def getAngle(self):
        return self.angle

    def getPow(self):
        return self.potencia

    def getPos(self):
        return self.rect.center

    def getPosX(self):
        return self.rect.centerx

    def getPosY(self):
        return self.rect.centery

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height

    def vivo(self):
        if self.life > 0:
            return True
        return False

    #############################
    def offsetx(self):
        # calcular la la posicion X dependiendo del angulo
        return int(math.cos(trans_ang_rad(self.angle)) * (self.mira.getWidht() / 2))

    def offsety(self):
        # calcular la la posicion Y dependiendo del angulo
        return int(math.sin(trans_ang_rad(self.angle)) * (self.mira.getWidht() / 2))

    # definir la interaccion con las teclas izq y der alteran el angulo y up y down alteran la potencia
    def izq_apretar(self):
        self.cambia_angulo = 1

    def der_apretar(self):
        self.cambia_angulo = -1

    def izq_soltar(self):
        self.cambia_angulo = 0

    def der_soltar(self):
        self.cambia_angulo = 0

    def up_apretar(self):
        self.cambia_potencia = 1

    def down_apretar(self):
        self.cambia_potencia = -1

    def up_soltar(self):
        self.cambia_potencia = 0

    def down_soltar(self):
        self.cambia_potencia = 0

    ###############################
    # cambiar el angulo y la potencia ademas de limitarlas a un rango
    def mover_angulo(self):
        if self.angle < 0:
            self.angle = 0

        elif self.angle > 180:
            self.angle = 180

        else:
            self.angle += self.cambia_angulo

    def cambio_potencia(self):

        if self.potencia < 10:
            self.potencia = 10
        elif self.potencia > 150:
            self.potencia = 150
        else:
            self.potencia += self.cambia_potencia

    def updateLife(self, resto):
        self.life = self.life - resto

    def actualiza_tanques(self, nuevo_y):
        self.corona.rect.center = [self.rect.centerx, self.rect.centery - 50]
        caida = nuevo_y + 9 - self.rect.bottom
        if caida > 0:
            self.life -= caida * caida / 400
        if nuevo_y >= datos.tamagno_mapa[1]:
            print("tanke eliminado por salir del mapa")
            self.life = -1
        self.rect.bottom = nuevo_y + 10

    def tiene_balas(self):
        if self.inventario1 == 0 and self.inventario2 == 0 and self.inventario3 == 0:
            return False
        return True

    def coronar(self):
        self.sprites.add(self.corona)

