import pygame
import random as r
import IA_aleatoria
from Tank import Tank
import datos as d


class Terreno:
    # mapas que fueron para pruebas

    # forma 1 = terreno casi liso
    # forma 2 = colina

    # mapas para entrega listos

    # forma 3 = 4 montañas
    # forma 4 = 2 montañas grandes
    # forma 5 = 3 montañas 2 cañones
    # forma 6 = 2 motañas disparejas 2 cañones

    forma_terreno = r.randint(1, 6)

    # lista de tanques en el mapa
    tanques = []

    # matris de alturas generadas al azar (es la mitad del largo del mapa)
    alturas = []

    # fin de ejecucion
    fin = False

    # variables para la creacion del terreno

    alternar_mod = 0
    lista_largo_mod = []
    distancia_rec = 0
    pos_lista_mod = 0
    altura_inicial = 0
    cantidad_diviciones = 0
    tipo_de_mod = 0

    # crear terreno
    def __init__(self):
        pass
        # construcctor vacio, usar funciones para cambiar cosas

    # ------modicadores de terreno---------

    def subida_1(self):
        alazar = r.randint(-7, 1)
        self.altura_inicial = self.altura_inicial + alazar
        # verificar
        if self.altura_inicial < 40:
            self.altura_inicial = 40

        self.alturas.append(self.altura_inicial)
        self.alternar_mod = self.alternar_mod + 1

    def mantener_0(self):
        alazar = r.randint(-2, 2)
        self.altura_inicial = self.altura_inicial + alazar
        # verificar suelo
        if self.altura_inicial > d.alto - 10:
            self.altura_inicial = d.alto - 10

        self.alturas.append(self.altura_inicial)
        self.alternar_mod = self.alternar_mod + 1

    def bajada_1(self):
        alazar = r.randint(-1, 7)
        self.altura_inicial = self.altura_inicial + alazar
        # verificar suelo
        if self.altura_inicial > d.alto - 20:
            self.altura_inicial = d.alto - 20

        self.alturas.append(self.altura_inicial)
        self.alternar_mod = self.alternar_mod + 1

    # ---------dividir terreno------------

    def dividir_terreno(self):

        for largo in range(self.cantidad_diviciones):
            distancia = d.largo_mitad // self.cantidad_diviciones - (
                    d.largo_mitad // self.cantidad_diviciones) // self.cantidad_diviciones
            self.lista_largo_mod.append(distancia)
            self.distancia_rec = self.distancia_rec + distancia

        dis_faltante = d.largo_mitad - self.distancia_rec
        self.lista_largo_mod.append(dis_faltante)

    # ------------guardar variables del terreno-------------

    def hacer_terreno(self, lista_mapa):

        self.dividir_terreno()

        for x in range(d.largo_mitad):  # largo del mapa

            # -----------cambio de modo de creacion de terreno--------------

            if self.lista_largo_mod[self.pos_lista_mod] == self.alternar_mod:
                self.tipo_de_mod = lista_mapa[self.pos_lista_mod]

                # print("cambio de modo a", self.tipo_de_mod)
                self.alternar_mod = 0
                self.pos_lista_mod = self.pos_lista_mod + 1

            # mod = solo subida    #subida es numeros negativos
            if self.tipo_de_mod == 1:
                self.subida_1()

            # mod = mantener
            elif self.tipo_de_mod == 0:
                self.mantener_0()

            # mod = solo bajar
            elif self.tipo_de_mod == -1:
                self.bajada_1()

        # -----------furturos modificadores de terreno------------

        # mod = mitad subir mitad bajar

        # mod = mitad bajar mitad subir

        # reinicia las variables
        self.alternar_mod = 0
        self.lista_largo_mod = []
        self.distancia_rec = 0
        self.pos_lista_mod = 0
        # print(self.lista_largo_mod)

    # ----------------funcion Genera terreno-------------------------

    def crea_terreno(self):

        self.forma_terreno = r.randint(3, 6)

        # -------------terreno 1- planicie -------------------
        if self.forma_terreno == 1:
            self.altura_inicial = 490

            # mapa de 15 modificaciones

            # 1 subida
            # 0 mantener
            # -1 bajada

            # --------------dibujar mapa-------------------
            self.tipo_de_mod = 0
            lista_mapa = []

            self.cantidad_diviciones = 1 - 1

            self.hacer_terreno(lista_mapa)

        # ---------------terreno 2- colina muerto hasta proxima actualiacion------------
        if self.forma_terreno == 2:
            self.altura_inicial = 490

            # mapa de 15 modificaciones

            # 1 subida
            # 0 mantener
            # -1 bajada

            # ---------------dibujar mapa--------------------
            self.tipo_de_mod = -1
            lista_mapa = []

            self.cantidad_diviciones = 1 - 1

            self.hacer_terreno(lista_mapa)

        # --------------terreno 3- 4 colinas------------------
        if self.forma_terreno == 3:
            self.altura_inicial = 490

            # mapa de 15 modificaciones

            # 1 subida
            # 0 mantener
            # -1 bajada

            # -----------------dibujar mapa-------------------
            self.tipo_de_mod = 1
            lista_mapa = [-1, 1, -1, 1, -1, 1, -1]

            self.cantidad_diviciones = 8 - 1

            self.hacer_terreno(lista_mapa)

        # ---------------terreno 4- 2 colinas-------------------

        # ------------------datos inciales-------------------------
        if self.forma_terreno == 4:
            self.altura_inicial = 490

            # mapa de 15 modificaciones

            # 1 subida
            # 0 mantener
            # -1 bajada

            # ----------------dibujar mapa-----------------------
            self.tipo_de_mod = 1
            lista_mapa = [0, -1, 0, 0, 1, 0, -1]

            self.cantidad_diviciones = 8 - 1

            self.hacer_terreno(lista_mapa)

        # --------------------terreno 5-  3 montañas 2 cañones----------------------------

        if self.forma_terreno == 5:

            # --------------------datos inciales------------------------------

            self.altura_inicial = 490

            # mapa de 15 modificaciones

            # 1 subida
            # 0 mantener
            # -1 bajada

            # -----------------------dibujar mapa-----------------------------------
            self.tipo_de_mod = 0
            lista_mapa = [1, -1, 0, -1, 1, 0, 1, -1, 0, -1, 1, 1, -1, 0]

            self.cantidad_diviciones = 15 - 1

            self.hacer_terreno(lista_mapa)

        # -----------------------terreno 6-  2 montañas disparejas y 2 cañones-------------------

        elif self.forma_terreno == 6:

            # ----------------datos inciales---------------------------

            self.altura_inicial = 510

            # mapa de 15 modificaciones

            # 1 subida
            # 0 mantener
            # -1 bajada

            # -------------------dibujar mapa-----------------------
            self.tipo_de_mod = 0
            lista_mapa = [1, 1, 0, -1, -1, 0, -1, 1, 0, 1, 0, -1, -1, 1]

            self.cantidad_diviciones = 15 - 1

            self.hacer_terreno(lista_mapa)

    # ----------------------------------fin de creacion mapas diferentes---------------------------------------------

    # --------------------funciones de datos y estadisticas (consola)----------------
    def mostrar_datos(self):  # muestra la lista de alturas
        for x in self.alturas:
            print(x)

    # funcion para obtener posicion eje x aleatorea #
    def posiscion_x_alazar(self):
        x = r.randint(0, d.largo_mitad - 1)
        return x

    def check_pos(self, screen, color, i):
        pygame.draw.line(screen, color, (i, d.alto), (i, 0), 2)  # usado para ver posicion en mapa al darle un punto

    def chech_largo(self, screen, color, i, x):  # usado para revisar las distancias entre los tanques
        pygame.draw.line(screen, color, (i, x), (i - d.largo_mitad, x), 2)
        pygame.draw.line(screen, color, (i, x), (i + d.largo_mitad, x), 2)

    # -----------------funciones de dibujado del terreno----------------------------

    def dibujar_terreno(self, screen, color):  # funcion usada para dibujar el terreno
        i = 0
        for palos in self.alturas:
            pygame.draw.line(screen, color, (i, d.alto), (i, palos), d.grosor)
            i = i + 2

            # ----------comentario dibujar_terreno---------

    # para dibujar es llamar esta funcion dentro del loop main
    # nesesita crear objeto terreno

    # ---------------------funciones de colicion de terreno---------------------

    # funcion que verifica colicion con terreno (cualquier cosa)

    def coliciona_terreno(self, pos_x, pos_y):  # sistema de colicion no usado
        if self.alturas[pos_x] < pos_y:
            # print("colicion")
            pass

    def colicion_bala(self, tanque):  # colicion usada para la bala con el terreno

        posx = tanque.bala.getPos_X() // 2
        posy = tanque.bala.getPos_Y()

        altura = self.alturas[posx]
        if posy > altura:
            # print("colicion terreno")

            tanque.bala.explotar_terreno()
            tanque.explosion.iniciar(tanque.bala.getPos(), tanque.bala.get_diametro())
            tanque.bala.detener()
            # introducir funciones que hagan cosas con la bala colicion

        if posx <= 1:
            tanque.explosion.iniciar(tanque.bala.getPos(), tanque.bala.get_diametro())
            tanque.bala.detener()

        if posx >= d.largo_mitad - 1:
            tanque.explosion.iniciar(tanque.bala.getPos(), tanque.bala.get_diametro())
            tanque.bala.detener()

    def colicion_tank(self):  # colicion usada para la bala y el tanque (falta mejorar para que sea dinamica)

        # tanque 1
        offsetX = self.tanques[0].getWidth() / 2
        offsetY = self.tanques[0].getHeight() / 2
        tank1x = self.tanques[0].getPosX()
        tank1y = self.tanques[0].getPosY()
        bala1x = self.tanques[0].bala.getPos_X()
        bala1y = self.tanques[0].bala.getPos_Y()
        # tanque 2
        bala2x = self.tanques[1].bala.getPos_X()
        bala2y = self.tanques[1].bala.getPos_Y()
        tank2x = self.tanques[1].getPosX()
        tank2y = self.tanques[1].getPosY()

        # destruccion tanque 1
        if ((tank1x - offsetX <= bala1x <= tank1x + offsetX) and (
                tank1y - offsetY <= bala1y <= tank1y + offsetY)):
            # print("tanque1 bala1")
            self.fin = True

        if ((tank1x - offsetX <= bala2x <= tank1x + offsetX) and (
                tank1y - offsetY <= bala2y <= tank1y + offsetY)):
            # print("tanque1 bala2")
            self.fin = True

        if ((tank2x - offsetX <= bala1x <= tank2x + offsetX) and (
                tank2y - offsetY <= bala1y <= tank2y + offsetY)):
            # print("tanque2 bala1")
            self.fin = True

        if ((tank2x - offsetX <= bala2x <= tank2x + offsetX) and (
                tank2y - offsetY <= bala2y <= tank2y + offsetY)):
            # print("tanque2 bala2")
            self.fin = True

    def colisionSprite(self, tank, bala, sonidoIm, sonidoDead):
        tankX = tank.getPosX()
        offsetX = tank.getWidth() / 2
        tankY = tank.getPosY()
        offsetY = tank.getHeight() / 2
        balax = bala.getPos_X()
        balay = bala.getPos_Y()
        cont = 0
        if (tankX - offsetX <= balax < tankX + offsetX) and (tankY - offsetY <= balay <= tankY + offsetY) and cont == 0:
            tank.explosion.iniciar(bala.getPos(), bala.get_diametro())
            bala.detener()
            tank.updateLife(bala.dagno)
            if tank.life <= 0:
                sonidoDead.play()
                self.fin = True
                return True
            else:
                sonidoIm.play()
                return False

    # ---------------------funciones que cambian el terreno-----------------------------

    # funcion que cambie linea espesifica cordenada x  (futura actualizacion)

    def destruir_terreno(self):
        for i in self.tanques:
            for j in range(len(i.bala.puntos_x)):

                pos_destruir = (i.bala.puntos_x[j]) // 2
                punto_y_pos = i.bala.puntos_ypos[j]
                punto_y_neg = i.bala.puntos_yneg[j]
                punto_y_distancia = i.bala.distancia_ypos_yneg[j]

                if self.alturas[pos_destruir] > punto_y_pos:
                    # print("no toco")
                    pass

                elif self.alturas[pos_destruir] < punto_y_neg:
                    self.alturas[pos_destruir] = self.alturas[pos_destruir] + punto_y_distancia
                    # print("esta arriba de mi")

                elif self.alturas[pos_destruir] > punto_y_neg:

                    self.alturas[pos_destruir] = punto_y_pos

                    # print("esta abajo de mi")

        for i in self.tanques:
            # pygame.draw.circle(display, self.rojo ,[i.bala.Fpos_balaX,i.bala.Fpos_balaY],10)

            i.bala.reinicia_lista()

    # ---------------------------funcion de generar tanques en el terreno-------------------------------
    def crear_tanque_pruebas(self):
        n_pos = 10

        Tanque = Tank(d.tanque(1), (n_pos * 2), (self.alturas[n_pos]), d.cagnon(1))
        self.tanques.append(Tanque)
        self.tanques.append(Tanque)

    def crear_tanque_pos(self):  # funcion usada para generar tanques en el terreno
        orden = IA_aleatoria.mezclar_lista(d.cantidad_tankes)
        n_tnks = d.cantidad_tankes
        espacio_por_tnk = d.tamagno_mapa[0] // (n_tnks*2 - 1)
        for i in range(n_tnks):
            self.matar_tanque(0)
        for i in range(n_tnks):
            n_pos = r.randint(20, espacio_por_tnk-20)
            n_pos += espacio_por_tnk * (orden[i]*2)
            n_pos = n_pos//2
            Tanque = Tank(d.tanque(i+1), (n_pos*2), self.alturas[n_pos], d.cagnon(i+1))
            self.tanques.append(Tanque)

    def dibujar_tanques(self, screen):  # funcion que dibuja tanques en pantalla
        for x in self.tanques:
            x.dibujar(screen)

    def matar_tanque(self, indice):  # destruir tanque por indice guardado por lista de tanques
        if len(self.tanques) == 0:
            print("no hay tanques")
        else:
            self.tanques.remove(self.tanques[indice])

    def actualiza_postanque(self):
        for i in self.tanques:
            i.actualiza_tanques(self.alturas[i.rect.centerx // 2])
