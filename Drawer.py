from IMG import  Img
import  datos
import pygame
import math
class Drawer:
        def __init__(self,tanques,pantalla):
            self.tanklist = tanques
            self.pantalla = pantalla
            # definir el texto en pantalla (potencia) como un sprite para poder manejarlo de manera mas rapida
            self.txtImg = datos.txt("potencia")
            self.distanImg = datos.txt("distancia")
            self.heightImg = datos.txt("altura")
            self.invenImg = datos.txt("balas")
            # definir las imagenes de los numeros en un arreglo donde el indice es el mismo que el numero de su imagen
            self.numImg = [datos.num(0), datos.num(1), datos.num(2), datos.num(3), datos.num(4), datos.num(5), datos.num(6),
                           datos.num(7), datos.num(8), datos.num(9)]
            # colocar el texto dependiendo donde esta el el tanque

            self.imgPower = Img(0, 50, self.txtImg)
            self.width_leter = self.imgPower.getWidth()
            self.cent = Img(0, 50, self.numImg[2])
            width_num = self.cent.getWidth()
                # poner la potencia en pantalla
            self.imgPower = Img(5 + self.width_leter / 2, 25, self.txtImg)
            self.cent = Img(15 + self.width_leter, 25, self.numImg[2])
            self.dec = Img(15 + self.width_leter + width_num, 25, self.numImg[2])
            self.uni = Img(15 + self.width_leter + width_num * 2, 25, self.numImg[2])
                # poner la altura en pantalla
            self.imgAltura = Img(5 + self.width_leter / 2, 50, self.heightImg)
            self.mil = Img(15 + self.width_leter, 50, self.numImg[2])
            self.cent1 = Img(15 + self.width_leter + width_num, 50, self.numImg[2])
            self.dec1 = Img(15 + self.width_leter + width_num * 2, 50, self.numImg[2])
            self.uni1 = Img(15 + self.width_leter + width_num * 3, 50, self.numImg[2])
                # poner la cuanta  distancia recorre  en pantalla
            self.imgDistan = Img(5 + self.width_leter / 2, 75, self.distanImg)
            self.mil2 = Img(15 + self.width_leter, 75, self.numImg[2])
            self.cent2 = Img(15 + self.width_leter + width_num, 75, self.numImg[2])
            self.dec2 = Img(15 + self.width_leter + width_num * 2, 75, self.numImg[2])
            self.uni2 = Img(15 + self.width_leter + width_num * 3, 75, self.numImg[2])

            self.inventario = Img(5 + self.width_leter / 2, 100, self.invenImg)
            self.balaImg = Img(self.width_leter, 100, datos.abrir(datos.carpeta_balas, tanques[0].bala.tipo))
            self.dec3 = Img(self.width_leter + width_num * 2, 100, self.numImg[0])
            self.uni3 = Img(self.width_leter + width_num * 3, 100, self.numImg[0])



            self.sprites = pygame.sprite.Group()
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
            self.sprites.add(self.inventario)
            self.sprites.add(self.dec3)
            self.sprites.add(self.uni3)
            self.sprites.add(self.balaImg)
        def dibujar(self,tanqueA):
            self.actualizar(tanqueA)
            self.sprites.draw(self.pantalla)
            for i in self.tanklist:
                if i.vivo():
                    i.sprites.draw(self.pantalla)
                    # dibujar barra de vida miniatura
                    if i.corona not in i.sprites:
                        pygame.draw.rect(self.pantalla, datos.ROJO,
                                         [i.getPosX() - i.getWidth() / 2, i.getPosY() - 35, i.getWidth(), 7])
                        pygame.draw.rect(self.pantalla, datos.VERDE, [i.getPosX() - i.getWidth() / 2, i.getPosY() - 35,
                                                             i.getWidth() * (i.life / 100), 7])

                    i.explosion.update(pygame.time.get_ticks())

                    i.mira.rect.centery = i.rect.centery - i.height / 4
                    i.mira.rect.centerx = i.rect.centerx

        def actualizar(self,tanqueA):
            # calcular el nuemero de la centena la decena y la unidad
            # para usarlo como indice en las imagenes de dichos sprites de la potencia
            centena = int(tanqueA.potencia // 100)
            decena = int((tanqueA.potencia % 100) // 10)
            unidad = int(((tanqueA.potencia % 100) % 10))
            ############################################################################################
            # calculos para la altura
            mil = int(tanqueA.bala.get_altura() // 1000)
            centena1 = int((tanqueA.bala.get_altura() % 1000) // 100)
            decena1 = int(((tanqueA.bala.get_altura() % 1000) % 100) // 10)
            unidad1 = int(((tanqueA.bala.get_altura() % 1000) % 100) % 10)
            #############################################################################################
            # Calculos para la distancia
            mil2 = int(math.fabs(tanqueA.bala.posxInicio - tanqueA.bala.posX) // 1000)
            centena2 = int((math.fabs(tanqueA.bala.posxInicio - tanqueA.bala.getPos_X()) % 1000) // 100)
            decena2 = int(((math.fabs(tanqueA.bala.posxInicio - tanqueA.bala.getPos_X()) % 1000) % 100) // 10)
            unidad2 = int(((math.fabs(tanqueA.bala.posxInicio - tanqueA.bala.getPos_X()) % 100) % 10))
            # calculo inventario
            if tanqueA.bala.tipo == "60mm.png":
                tanqueA.inventarioF = tanqueA.inventario1
            if tanqueA.bala.tipo == "perforante.png":
                tanqueA.inventarioF = tanqueA.inventario2
            if tanqueA.bala.tipo == "105mm.png":
                tanqueA.inventarioF = tanqueA.inventario3
            if tanqueA.inventarioF == 0:
                tanqueA.disparable = False
            else:
                tanqueA.disparable = True

            decena3 = int(tanqueA.inventarioF // 10)
            unidad3 = int(tanqueA.inventarioF % 10)
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
            rotada_img, rotada_pos = tanqueA.mira.rotar(tanqueA.mira.imagenR, tanqueA.angle)
            tanqueA.mira.image = rotada_img
            tanqueA.mira.rect = rotada_pos

            # cambiar bala e inventario
            balaT = tanqueA.bala.tipo
            self.balaImg.camb(datos.abrir(datos.carpeta_balas, balaT))
            self.dec3.camb(self.numImg[decena3])
            self.uni3.camb(self.numImg[unidad3])
            # borrar fonndo imagen

            tanqueA.mira.image.set_colorkey(datos.BLANCO)
            # recorrer las posiciones donde estuvo la bala y imprimir un punto
            for c in tanqueA.bala.coordinate:
                pygame.draw.circle(self.pantalla, datos.AZUL, c, 2)
            # actualizar posicion de la bala si esta esta visible

            if tanqueA.sprites.has(tanqueA.bala):
                tanqueA.bala.update()


