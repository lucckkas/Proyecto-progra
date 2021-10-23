import pygame, math
import datos
from Bala import Bala
from Mira import Mira
from IMG import Img
from Explosion import Explosion
from Bala60 import Bala60
from BalaP import  BalaP
from Bala105 import Bala105
TAM_MAPA = 1280


# transformar de grados a radianes
def trans_ang_rad(ang):
    return ang * math.pi / 180


class Tank(pygame.sprite.Sprite):
    def __init__(self, Imagen, posX, posY, miraImg):
        super().__init__()
        self.image = pygame.image.load(Imagen)
        # borrar fonndo imagen
        self.image.set_colorkey(datos.BLANCO)
        self.rect = self.image.get_rect()
        self.rect.centerx = posX
        self.rect.centery = posY
        self.height = self.image.get_height()
        self.width = self.image.get_width()
        self.potencia = 30
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
        self.bala = Bala60()
        self.explosion = Explosion()

        # definir el texto en pantalla (potencia) como un sprite para poder manejarlo de manera mas rapida
        self.txtImg = datos.txt("potencia")
        self.distanImg = datos.txt("distancia")
        self.heightImg = datos.txt("altura")
        self.invenImg = datos.txt("balas")
        # definir las imagenes de los numeros en un arreglo donde el indice es el mismo que el numero de su imagen
        self.numImg = [datos.num(0), datos.num(1), datos.num(2), datos.num(3), datos.num(4), datos.num(5), datos.num(6),
                       datos.num(7), datos.num(8), datos.num(9)]
        # colocar el texto dependiendo donde esta el el tanque
        if self.rect.centerx > 640:
            # crear una imagen del texto y de la centena para poder obtener sus anchos y crearlos en la posicion adecuada
            # con un calculo que use dichas variables y el tamaño de la pantalla
            self.imgPower = Img(0, 50, self.txtImg)
            width_leter = self.imgPower.getWidth()
            self.cent = Img(0, 50, self.numImg[2])
            width_num = self.cent.getWidth() + 1
            # volver a crear las imagenes solo que ahora con su posicion correcta
            self.imgPower = Img((TAM_MAPA - (width_leter / 2) - (width_num) * 3), 25, self.txtImg)
            self.cent = Img((TAM_MAPA - (width_num) * 3), 25, self.numImg[0])
            self.dec = Img((TAM_MAPA - (width_num) * 2), 25, self.numImg[2])
            self.uni = Img((TAM_MAPA - (width_num)), 25, self.numImg[2])
            # poner la altura en pantalla
            self.imgAltura = Img((TAM_MAPA - (width_leter / 2) - (width_num) * 4), 50, self.heightImg)
            self.mil = Img((TAM_MAPA - (width_num) * 4), 50, self.numImg[0])
            self.cent1 = Img((TAM_MAPA - (width_num) * 3), 50, self.numImg[0])
            self.dec1 = Img((TAM_MAPA - (width_num) * 2), 50, self.numImg[2])
            self.uni1 = Img((TAM_MAPA - (width_num)), 50, self.numImg[2])
            # poner la cuanta  distancia recorre  en pantalla
            self.imgDistan = Img((TAM_MAPA - (width_leter / 2) - (width_num) * 4), 75, self.distanImg)
            self.mil2 = Img((TAM_MAPA - (width_num) * 4), 75, self.numImg[0])
            self.cent2 = Img((TAM_MAPA - (width_num) * 3), 75, self.numImg[0])
            self.dec2 = Img((TAM_MAPA - (width_num) * 2), 75, self.numImg[2])
            self.uni2 = Img((TAM_MAPA - (width_num)), 75, self.numImg[2])
            #
            self.inventario = Img(TAM_MAPA - width_leter / 2 - width_num * 4, 100, self.invenImg)
            self.balatip = self.bala.tipo

            self.balaImg = Img(TAM_MAPA - width_num * 4, 100, datos.abrir(datos.carpeta_balas, self.balatip))
            self.dec3 = Img(TAM_MAPA - width_num * 2, 100, self.numImg[0])
            self.uni3 = Img(TAM_MAPA - width_num, 100, self.numImg[0])
            #
            self.posvidaX = (TAM_MAPA - self.wLife) - 1
            self.posvidaY = 125

        else:
            # repetir lo mismo solo que ajustando la posiciones
            self.imgPower = Img(0, 50, self.txtImg)
            width_leter = self.imgPower.getWidth()
            self.cent = Img(0, 50, self.numImg[2])
            width_num = self.cent.getWidth()
            # poner la potencia en pantalla
            self.imgPower = Img(0 + width_leter / 2, 25, self.txtImg)
            self.cent = Img(0 + width_leter, 25, self.numImg[2])
            self.dec = Img(0 + width_leter + width_num, 25, self.numImg[2])
            self.uni = Img(0 + width_leter + width_num * 2, 25, self.numImg[2])
            # poner la altura en pantalla
            self.imgAltura = Img(0 + width_leter / 2, 50, self.heightImg)
            self.mil = Img(0 + width_leter, 50, self.numImg[2])
            self.cent1 = Img(0 + width_leter + width_num, 50, self.numImg[2])
            self.dec1 = Img(0 + width_leter + width_num * 2, 50, self.numImg[2])
            self.uni1 = Img(0 + width_leter + width_num * 3, 50, self.numImg[2])
            # poner la cuanta  distancia recorre  en pantalla
            self.imgDistan = Img(0 + width_leter / 2, 75, self.distanImg)
            self.mil2 = Img(0 + width_leter, 75, self.numImg[2])
            self.cent2 = Img(0 + width_leter + width_num, 75, self.numImg[2])
            self.dec2 = Img(0 + width_leter + width_num * 2, 75, self.numImg[2])
            self.uni2 = Img(0 + width_leter + width_num * 3, 75, self.numImg[2])

            self.inventario = Img(0 + width_leter / 2, 100, self.invenImg)
            self.balatip = self.bala.tipo
            self.balaImg = Img(width_leter, 100, datos.abrir(datos.carpeta_balas, self.balatip))
            self.dec3 = Img(width_leter + width_num * 2, 100, self.numImg[0])
            self.uni3 = Img(width_leter + width_num * 3, 100, self.numImg[0])

            self.posvidaX = 0
            self.posvidaY = 125
        self.turn = True
        self.alive = True
        # crear la mira en su posicion correspondiente al centro en x y en su posicion y correspondiente
        self.mira = Mira(self.rect.x + self.width / 2, self.rect.y + self.height / 4.5, miraImg)
        self.bala = Bala60()
        # crear grupo donde estaran los sprites a dibujar
        self.sprites = pygame.sprite.Group()

        # agregar los elementos visibles
        self.sprites.add(self)
        self.sprites.add(self.imgPower)
        self.sprites.add(self.cent)
        self.sprites.add(self.dec)
        self.sprites.add(self.uni)
        self.sprites.add(self.imgAltura)
        self.sprites.add(self.mil)
        self.sprites.add(self.cent1)
        self.sprites.add(self.dec1)
        self.sprites.add(self.uni1)
        self.sprites.add(self.imgDistan)
        self.sprites.add(self.mil2)
        self.sprites.add(self.cent2)
        self.sprites.add(self.dec2)
        self.sprites.add(self.uni2)
        self.sprites.add(self.mira)
        self.sprites.add(self.inventario)
        self.sprites.add(self.balaImg)
        self.sprites.add(self.explosion)
        self.sprites.add(self.dec3)
        self.sprites.add(self.uni3)

    def dibujar(self, pantalla):

        self.explosion.update(pygame.time.get_ticks())

        self.mira.rect.centery = self.rect.centery - self.height / 4
        self.mira.rect.centerx = self.rect.centerx
        # calcular el nuemero de la centena la decena y la unidad para usarlo como indice en las imagenes de dichos sprites de la potencia
        centena = int(self.potencia // 100)
        decena = int((self.potencia % 100) // 10)
        unidad = int(((self.potencia % 100) % 10))
        ############################################################################################
        # calculos para la altura
        mil = int(self.bala.get_altura() // 1000)
        centena1 = int((self.bala.get_altura() % 1000) // 100)
        decena1 = int(((self.bala.get_altura() % 1000) % 100) // 10)
        unidad1 = int(((self.bala.get_altura() % 1000) % 100) % 10)
        #############################################################################################
        # Calculos para la distancia
        mil2 = int(math.fabs(self.bala.posxInicio - self.bala.posX) // 1000)
        centena2 = int((math.fabs(self.bala.posxInicio - self.bala.posX) % 1000) // 100)
        decena2 = int(((math.fabs(self.bala.posxInicio - self.bala.posX) % 1000) % 100) // 10)
        unidad2 = int(((math.fabs(self.bala.posxInicio - self.bala.posX) % 100) % 10))
        # calculo inventario
        if (self.bala.tipo == "60mm.png"):
            self.inventarioF = self.inventario1
        if (self.bala.tipo == "perforante.png"):
            self.inventarioF = self.inventario2
        if (self.bala.tipo == "105mm.png"):
            self.inventarioF = self.inventario3
        if (self.inventarioF == 0):
            self.disparable = False
        else:
            self.disparable = True

        decena3 = int(self.inventarioF // 10)
        unidad3 = int(self.inventarioF % 10)

        # dibujar barra de vida
        pygame.draw.rect(pantalla, datos.ROJO, [self.posvidaX, self.posvidaY, 200, 30])
        pygame.draw.rect(pantalla, datos.VERDE, [self.posvidaX, self.posvidaY, 200 * (self.life / 100), 30])

        # cambiar la imagen dependiendo del indice
        # cambiar potencia
        self.cent.camb(self.numImg[centena])
        self.dec.camb(self.numImg[decena])
        self.uni.camb(self.numImg[unidad])
        # cambiar altura
        self.mil.camb(self.numImg[mil])
        self.cent1.camb(self.numImg[centena1])
        self.dec1.camb(self.numImg[decena1])
        self.uni1.camb(self.numImg[unidad1])
        # cambiar distancia
        self.mil2.camb(self.numImg[mil2])
        self.cent2.camb(self.numImg[centena2])
        self.dec2.camb(self.numImg[decena2])
        self.uni2.camb(self.numImg[unidad2])
        # hacer rotar la mira dependiendo del angulo
        rotada_img, rotada_pos = self.mira.rotar(self.mira.imagenR, self.angle)
        self.mira.image = rotada_img
        self.mira.rect = rotada_pos

        # cambiar bala e inventario
        balaT = self.bala.tipo

        self.balaImg.camb(datos.abrir(datos.carpeta_balas, balaT))
        self.dec3.camb(self.numImg[decena3])
        self.uni3.camb(self.numImg[unidad3])
        # borrar fonndo imagen

        self.mira.image.set_colorkey(datos.BLANCO)

        # recorrer las posiciones donde estuvo la bala y imprimir un punto
        for c in self.bala.coordinate:
            pygame.draw.circle(pantalla, datos.AZUL, c, 2)
        # actualizar posicion de la bala si esta esta visible
        if (self.sprites.has(self.bala)):
            self.bala.update()

        # dibujar los sprites que esten en el grupo
        self.sprites.draw(pantalla)

    def disparar(self):
        # disparar la bala dependiendo desde la punta de la mira
        if self.turn and self.disparable:
            # agregar la bala a los sprites visibles
            self.sprites.add(self.bala)
            if (self.bala.tipo == "60mm.png" and self.inventario1 > 0):
                self.inventario1 += -1
            if (self.bala.tipo == "perforante.png" and self.inventario2 > 0):
                self.inventario2 += -1
            if (self.bala.tipo == "105mm.png" and self.inventario3 > 0):
                self.inventario3 += -1

            # posicionar la bala en la mira usadando un offset en X y en Y
            self.bala.disparar(self.angle, self.potencia, self.mira.rect.centerx + self.offsetx(),
                               self.mira.rect.centery - self.offsety())

    # Retornar valores del tanque
    def getAngle(self):
        return self.angle

    def getPow(self):
        return self.potencia

    def getPosX(self):
        return self.rect.centerx

    def getPosY(self):
        return self.rect.centery

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height

    #############################
    def offsetx(self):
        # calcular la la posicion X dependiendo del angulo
        return int(math.cos(trans_ang_rad(self.angle)) * (self.mira.getWidht() / 2))

    def offsety(self):
        # calcular la la posicion Y dependiendo del angulo
        return int(math.sin(trans_ang_rad(self.angle)) * (self.mira.getWidht() / 2))

    def changeTurn(self):

        if self.turn == True:
            self.bala.disparado = False
            self.turn = False
        else:
            self.bala.disparado = False
            self.turn = True

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
        if (self.angle < 0):
            self.angle = 0

        elif (self.angle > 180):
            self.angle = 180

        else:
            self.angle += self.cambia_angulo

    def cambio_potencia(self):

        if (self.potencia < 10):
            self.potencia = 10
        elif (self.potencia > 150):
            self.potencia = 150
        else:
            self.potencia += self.cambia_potencia

    def updateLife(self, resto):
        self.life = self.life - resto

    def actualiza_tanques(self, nuevo_x):
        self.rect.centery = nuevo_x