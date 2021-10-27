import pygame
import sys
import datos
from menu import *
import Terreno
import Boton
import Bandera
import IA_aleatoria
from Bala60 import Bala60
from BalaP import BalaP
from Bala105 import Bala105
from IMG import Img
from Bala import Bala


class Game():  # Creación clase juego

    def __init__(self):

        pygame.init()  # Inicio de PYGAME en archivo local

        # limitar FPS
        self.clock = pygame.time.Clock()

        ### crear terreno ###
        self.mapa = Terreno.Terreno()
        self.mapa.crea_terreno()

        self.mapa.crear_tanque_pos()
        self.mapa.crear_tanque_pos()
        # definir que solo uno no podra tirar
        self.mapa.tanques[1].changeTurn()

        self.running, self.playing = True, False  # Definición variables para inicializacion de juego
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False  # Control de teclas
        self.DISPLAY_W, self.DISPLAY_H = datos.tamagno_mapa  # Definicion altura y ancho del canvas
        self.display = pygame.Surface(
            (self.DISPLAY_W, self.DISPLAY_H))  # Creacion canvas, recibe atura y ancho como argumentos
        self.window = pygame.display.set_mode(((self.DISPLAY_W, self.DISPLAY_H)))
        self.font_name = datos.abrir(datos.carpeta_archivos,
                                     "8BITWONDERNominal.ttf")  # Definición tipo de fuente (8-bit)
        self.main_menu = MainMenu(self)
        self.controls = MenuControles(self)
        self.credits = MenuCreditos(self)
        self.curr_menu = self.main_menu  # Permite visualizar distintos tipos de meus
        self.velocidad_mira = 0
        self.velocidad_potencia = 0
        # importacion de sonidos
        pygame.mixer.music.load(datos.abrir(datos.carpeta_sonidos, "music.mp3"))
        self.bala1Sound = pygame.mixer.Sound(datos.abrir(datos.carpeta_sonidos, "B4VDROP.wav"))
        self.bala2Sound = pygame.mixer.Sound(datos.abrir(datos.carpeta_sonidos, "B4VFBOMB.wav"))
        self.bala3Sound = pygame.mixer.Sound(datos.abrir(datos.carpeta_sonidos, "B4VAPIAS.wav"))
        self.greatSound = pygame.mixer.Sound(datos.abrir(datos.carpeta_sonidos, "B4VGREAT.wav"))
        self.hellSound = pygame.mixer.Sound(datos.abrir(datos.carpeta_sonidos, "B4VHELL.wav"))
        self.bala1Sound.set_volume(datos.Vbala1)
        self.bala2Sound.set_volume(datos.Vbala2)
        self.bala3Sound.set_volume(datos.Vbala3)
        self.greatSound.set_volume(datos.VGreat)
        self.hellSound.set_volume(datos.VHell)
        pygame.mixer.music.set_volume(datos.VMusica)

        # botones
        self.boton_reset = Boton.Boton("reset.png", [datos.tamagno_mapa[0] / 2, 40], [200, 60])
        self.boton_salir = Boton.Boton("salir.png", [datos.tamagno_mapa[0] / 2, 110], [200, 60])

        # para saber cual tanque es controlado por usuario y cual por "IA"
        self.cantidad_human = datos.cantidad_tankes - datos.cantidad_IA
        self.control_tankes = []
        self.IAs = []
        for i in range(self.cantidad_human):
            self.control_tankes.append(False)
        for i in range(datos.cantidad_IA):
            self.control_tankes.append(True)
            self.IAs.append(IA_aleatoria.IA_aleatoria())

        # bandera
        self.bandera = Bandera.Bandera([datos.tamagno_mapa[0] / 4, 10])

    def game_loop(self):  # Inicio loopeo
        pygame.mixer.music.play()
        while self.playing:  # Mientras siga jugando:
            self.check_events()  # Llamado a que checkee eventos

            if self.START_KEY:
                self.playing = False

            if (self.mapa.fin):
                break

            self.display.fill(datos.BLANCO)  # Rellena el canvas de color blanco

            # dibujar terreno
            self.mapa.dibujar_terreno(self.display, datos.NEGRO)

            # imprimir empate si es que es el caso
            if (self.mapa.tanques[1].inventario1 == 0 and self.mapa.tanques[1].inventario2 == 0 and self.mapa.tanques[
                1].inventario3 == 0 and self.mapa.tanques[0].life > 0 and self.mapa.tanques[1].life > 0 and
                    self.mapa.tanques[1].bala.disparado == False):
                empateI = Img(datos.tamagno_mapa[0] / 2, datos.tamagno_mapa[1] / 2,
                              datos.abrir(datos.carpeta_texto, "empate.png"))
                self.display.blit(empateI.image, (datos.tamagno_mapa[0] / 2 - empateI.getWidth() / 2,
                                                  datos.tamagno_mapa[1] / 2 + empateI.getHeight() / 2))
            # dibujar tanques
            self.mapa.dibujar_tanques(self.display)
            # dibujar botones
            self.boton_reset.dibujar(self.display)
            self.boton_salir.dibujar(self.display)
            self.bandera.dibujar(self.display, pygame.time.get_ticks())

            # pruebas lineas en centro
            # self.mapa.check_pos(self.display, self.rojo, 560)
            # self.mapa.check_pos(self.display, self.rojo, 720)
            # self.mapa.check_pos(self.display, self.rojo, 640)

            # pruebas distancia entre tanques
            # self.mapa.chech_largo(self.display, self.rojo, self.mapa.tanques[0].rect.x, self.mapa.tanques[0].rect.y)

            # pruebas deteccion explocion de terreno

            """
            for i in range(len(self.mapa.tanques[0].bala.puntos_x)):
                pygame.draw.circle(self.display,self.rojo,[self.mapa.tanques[0].bala.puntos_x[i],self.mapa.tanques[0].bala.Fpos_balaY],2)
            
                pygame.draw.circle(self.display,self.rojo,[self.mapa.tanques[0].bala.puntos_x[i],self.mapa.tanques[0].bala.puntos_ypos[i]],2)
           
                pygame.draw.circle(self.display,self.rojo,[self.mapa.tanques[0].bala.puntos_x[i],self.mapa.tanques[0].bala.puntos_yneg[i]],2)
            """

            # destruir terreno
            self.mapa.destruir_terreno(self.display)

            # actualizar posision tanque
            self.mapa.actualiza_postanque()

            # colicion de balas

            # colicion tank_bullet
            # self.mapa.colicion_tank()

            #For definitivo poner dentro todas las mapa.tanques

            for i in self.mapa.tanques:
                self.mapa.colicion_bala(i)
                i.mover_angulo()
                i.cambio_potencia()
                for j in self.mapa.tanques:
                    self.mapa.colisionSprite(i, j.bala, self.greatSound,self.hellSound)


            self.window.blit(self.display, (0, 0))  # Alinea display y window -no borrar-



            pygame.display.update()  # Mueve fisicamente la imagen a la pantalla
            self.reset_keys()  # Llamado a funcion que resetea los controles
            self.clock.tick(datos.FPS)

            # reinicio del mundo
        self.mapa.fin = False
        self.mapa.alturas = []
        self.mapa.crea_terreno()
        self.mapa.matar_tanque(1)
        self.mapa.matar_tanque(0)
        self.mapa.crear_tanque_pos()
        self.mapa.crear_tanque_pos()
        self.mapa.tanques[1].changeTurn()

    def check_events(self):  # Checkea que botones presiona el usuario
        # disparo por "IA"
        for i in range(datos.cantidad_IA):
            j = i + self.cantidad_human
            if self.mapa.tanques[j].turn and not self.mapa.tanques[j].bala.disparado:
                if self.control_tankes[j]:  # si el tanque es controlado por "IA"
                    self.mapa.tanques[j].dispararIA(self.IAs[i].disparar())

        for event in pygame.event.get():  # Muestra lo que ve el usuario en pantalla (in-game)

            if event.type == pygame.QUIT:  # Cuando presione la "X" cierra el juego y pygame
                self.running, self.playing = False, False  # Cierra juego
                self.curr_menu.run_display = False
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.boton_reset.click(pygame.mouse.get_pos()):
                    self.START_KEY = True

                if self.boton_salir.click(pygame.mouse.get_pos()):
                    self.running, self.playing = False, False  # Cierra juego
                    self.curr_menu.run_display = False
                    sys.exit()

            if event.type == pygame.KEYDOWN:  # Revisa si sigue en el juego

                if event.key == pygame.K_RETURN:
                    self.START_KEY = True

                if event.key == pygame.K_BACKSPACE:
                    self.BACK_KEY = True

                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True

                if event.key == pygame.K_UP:
                    self.UP_KEY = True

                ##########   teclas para hacer pruebas de funcionamiento  ###############
                if event.key == pygame.K_n:
                    self.mapa.crear_tanque_pos()  # actualizar despues

                if event.key == pygame.K_m:  # mata tanque en el indice 0
                    self.mapa.matar_tanque(0)

                if event.key == pygame.K_SPACE:
                    # si es turno del 1 tanque
                    if self.mapa.tanques[0].turn and not self.mapa.tanques[0].bala.disparado:
                        self.mapa.tanques[0].disparar()

                    # si es turno del 2 tanque
                    if self.mapa.tanques[1].turn and not self.mapa.tanques[1].bala.disparado:
                        self.mapa.tanques[1].disparar()

                if event.key == pygame.K_1:
                    if self.mapa.tanques[0].turn and self.mapa.tanques[0].bala.disparado == False:
                        self.mapa.tanques[0].bala = Bala60()
                        self.bala1Sound.play()
                    if self.mapa.tanques[1].turn and self.mapa.tanques[1].bala.disparado == False:
                        self.mapa.tanques[1].bala = Bala60()
                        self.bala1Sound.play()

                if event.key == pygame.K_2:
                    if self.mapa.tanques[0].turn and self.mapa.tanques[0].bala.disparado == False:
                        self.mapa.tanques[0].bala = BalaP()
                        self.bala2Sound.play()
                    if self.mapa.tanques[1].turn and self.mapa.tanques[1].bala.disparado == False:
                        self.mapa.tanques[1].bala = BalaP()
                        self.bala2Sound.play()

                if event.key == pygame.K_3:
                    if self.mapa.tanques[0].turn and self.mapa.tanques[0].bala.disparado == False:
                        self.mapa.tanques[0].bala = Bala105()
                        self.bala3Sound.play()
                    if self.mapa.tanques[1].turn and self.mapa.tanques[1].bala.disparado == False:
                        self.mapa.tanques[1].bala = Bala105()
                        self.bala3Sound.play()

                # mover tanque 1
                # angulo

                if event.key == pygame.K_LEFT:
                    if self.mapa.tanques[0].turn and self.mapa.tanques[0].bala.disparado == False:
                        self.mapa.tanques[0].izq_apretar()
                    if self.mapa.tanques[1].turn and self.mapa.tanques[1].bala.disparado == False:
                        self.mapa.tanques[1].izq_apretar()
                if event.key == pygame.K_RIGHT:
                    if self.mapa.tanques[0].turn and self.mapa.tanques[0].bala.disparado == False:
                        self.mapa.tanques[0].der_apretar()
                    if self.mapa.tanques[1].turn and self.mapa.tanques[1].bala.disparado == False:
                        self.mapa.tanques[1].der_apretar()
                # potencia
                if event.key == pygame.K_UP:
                    if self.mapa.tanques[0].turn and self.mapa.tanques[0].bala.disparado == False:
                        self.mapa.tanques[0].up_apretar()
                    if self.mapa.tanques[1].turn and self.mapa.tanques[1].bala.disparado == False:
                        self.mapa.tanques[1].up_apretar()

                if event.key == pygame.K_DOWN:
                    if self.mapa.tanques[0].turn and self.mapa.tanques[0].bala.disparado == False:
                        self.mapa.tanques[0].down_apretar()
                    if self.mapa.tanques[1].turn and self.mapa.tanques[1].bala.disparado == False:
                        self.mapa.tanques[1].down_apretar()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    if self.mapa.tanques[0].turn and self.mapa.tanques[0].bala.disparado == False:
                        self.mapa.tanques[0].izq_soltar()
                    if self.mapa.tanques[1].turn and self.mapa.tanques[1].bala.disparado == False:
                        self.mapa.tanques[1].izq_soltar()
                if event.key == pygame.K_RIGHT:
                    if self.mapa.tanques[0].turn and self.mapa.tanques[0].bala.disparado == False:
                        self.mapa.tanques[0].der_soltar()
                    if self.mapa.tanques[1].turn and self.mapa.tanques[1].bala.disparado == False:
                        self.mapa.tanques[1].der_soltar()
                # potencia
                if event.key == pygame.K_UP:
                    if self.mapa.tanques[0].turn and self.mapa.tanques[0].bala.disparado == False:
                        self.mapa.tanques[0].up_soltar()
                    if self.mapa.tanques[1].turn and self.mapa.tanques[1].bala.disparado == False:
                        self.mapa.tanques[1].up_soltar()

                if event.key == pygame.K_DOWN:
                    if self.mapa.tanques[0].turn and self.mapa.tanques[0].bala.disparado == False:
                        self.mapa.tanques[0].down_soltar()
                    if self.mapa.tanques[1].turn and self.mapa.tanques[1].bala.disparado == False:
                        self.mapa.tanques[1].down_soltar()

    def reset_keys(self):  # Resetea los controles
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False

    def dibuja_texto(self, text, size, x, y):  # Recibe como argumentos las caracteristicas del texto
        font = pygame.font.Font(self.font_name,
                                size)  # Define a la fuente como una variable que recibe el nombre y el tamaño
        text_surface = font.render(text, True, datos.NEGRO)  # Crea una imagen rectangular de la imagen de texto
        text_rect = text_surface.get_rect()  # crea dimensiones del "rectangulo"
        text_rect.center = (x, y)  # Centra la imagen del rectangulo
        self.display.blit(text_surface,
                          text_rect)  # Pone el rectangulo con la imagen que contiene el texto en la imagen


