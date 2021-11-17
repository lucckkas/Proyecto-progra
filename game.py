import pygame
import sys

import Triangulo
import datos
from menu import *
import Terreno
import Boton
import Bandera
import IA_aleatoria
from IMG import Img
from Bala import Bala


class Game:  # Creación clase juego

    def __init__(self):

        pygame.init()  # Inicio de PYGAME en archivo local
        # limitar FPS
        self.clock = pygame.time.Clock()

        # sistema turnos
        self.turnos = IA_aleatoria.mezclar_lista(datos.cantidad_tankes)
        self.turno_act = self.turnos[0]

        # -----------crear terreno-----------
        self.mapa = Terreno.Terreno()
        self.mapa.crea_terreno()

        self.mapa.crear_tanque_pos()

        self.running, self.playing = True, False  # Definición variables para inicializacion de juego
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False  # Control de teclas
        self.DISPLAY_W, self.DISPLAY_H = datos.tamagno_mapa  # Definicion altura y ancho del canvas
        self.display = pygame.Surface(
            (self.DISPLAY_W, self.DISPLAY_H))  # Creacion canvas, recibe atura y ancho como argumentos
        self.window = pygame.display.set_mode((self.DISPLAY_W, self.DISPLAY_H))
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

        self.ultimo_tiro = 0  # lleva el tiempo para limitar que tan seguido disparan

        # bandera
        self.bandera = Bandera.Bandera([datos.tamagno_mapa[0]*3 / 4, 10])

        # triangulo para los turnos
        self.triangulo = Triangulo.Triangulo(self.mapa.tanques[self.turno_act].getPos())

        # mostrar info tank actual
        # self.mapa.tanques[self.turno_act].Aparametros(self.display)

    def game_loop(self):  # Inicio loopeo
        pygame.mixer.music.play()
        while self.playing:  # Mientras siga jugando:
            # destruir terreno
            self.mapa.destruir_terreno()

            # actualizar posision tanque
            self.mapa.actualiza_postanque()

            self.check_events()  # Llamado a que checkee eventos

            if self.START_KEY:
                self.playing = False

            if self.mapa.fin:
                break

            self.display.fill(datos.BLANCO)  # Rellena el canvas de color blanco

            # dibujar terreno
            self.mapa.dibujar_terreno(self.display, datos.NEGRO)

            if self.cantidad_human == 1000:  # FIXME no funciona, los tankes que mueren antes no disparan
                empateI = Img(datos.tamagno_mapa[0] / 2, datos.tamagno_mapa[1] / 2,
                              datos.abrir(datos.carpeta_texto, "empate.png"))
                self.display.blit(empateI.image, (datos.tamagno_mapa[0] / 2 - empateI.getWidth() / 2,
                                                  datos.tamagno_mapa[1] / 2 + empateI.getHeight() / 2))

            # dibujar tanques
            self.mapa.dibujar_tanques(self.display)


            # dibujar botones
            self.boton_reset.dibujar(self.display)
            self.boton_salir.dibujar(self.display)
            # dibuja bandera
            self.bandera.dibujar(self.display, pygame.time.get_ticks())
            # dibuja triangulo para los turnos
            self.triangulo.dibujar(self.display, pygame.time.get_ticks())

            # For definitivo poner dentro todas las mapa.tanques
            for i in self.mapa.tanques:
                if self.mapa.colicion_bala(i):
                    self.sig_turno()
                i.mover_angulo()
                i.cambio_potencia()
                for j in self.mapa.tanques:
                    if self.mapa.colisionSprite(i, j.bala, self.greatSound, self.hellSound):
                        self.sig_turno()

            self.window.blit(self.display, (0, 0))  # Alinea display y window -no borrar-

            pygame.display.update()  # Mueve fisicamente la imagen a la pantalla
            self.reset_keys()  # Llamado a funcion que resetea los controles
            self.clock.tick(datos.FPS)

            # disparo por "IA"
            if self.turno_act >= self.cantidad_human:
                if not self.mapa.tanques[self.turno_act].bala.disparado\
                        and pygame.time.get_ticks() - self.ultimo_tiro > 500\
                        and self.mapa.tanques[self.turno_act].vivo():
                    self.mapa.tanques[self.turno_act].dispararIA(
                        self.IAs[self.turno_act - self.cantidad_human].disparar())

            # reinicio del mundo
        self.mapa.fin = False
        self.mapa.alturas = []
        self.mapa.crea_terreno()
        for i in range(datos.cantidad_tankes):
            self.mapa.matar_tanque(0)
        self.mapa.crear_tanque_pos()

    def check_events(self):  # Checkea que botones presiona el usuario

        for event in pygame.event.get():  # Muestra lo que ve el usuario en pantalla (in-game)

            if event.type == pygame.QUIT:  # Cuando presione la "X" cierra el juego y pygame
                self.running, self.playing = False, False  # Cierra juego
                self.curr_menu.run_display = False
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.boton_reset.click(pygame.mouse.get_pos()):
                    self.START_KEY = True
                    # reinicio turnos
                    self.turnos = IA_aleatoria.mezclar_lista(datos.cantidad_tankes)
                    self.turno_act = self.turnos[0]
                    self.triangulo.mover(self.mapa.tanques[self.turno_act].getPos())
                    self.mapa.tanques[self.turno_act].Aparametros(self.display)

                if self.boton_salir.click(pygame.mouse.get_pos()):
                    self.running, self.playing = False, False  # Cierra juego
                    self.curr_menu.run_display = False
                    sys.exit()

            if event.type == pygame.KEYDOWN:  # Revisa si sigue en el juego

                if event.key == pygame.K_RETURN:
                    self.START_KEY = True
                    # reinicio turnos
                    self.turnos = IA_aleatoria.mezclar_lista(datos.cantidad_tankes)
                    self.turno_act = self.turnos[0]
                    self.triangulo.mover(self.mapa.tanques[self.turno_act].getPos())
                    self.mapa.tanques[self.turno_act].Aparametros(self.display)

                if event.key == pygame.K_BACKSPACE:
                    self.BACK_KEY = True

                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True

                if event.key == pygame.K_UP:
                    self.UP_KEY = True

                # --------------------teclas para hacer pruebas de funcionamiento------------------------
                if event.key == pygame.K_n:
                    self.mapa.crear_tanque_pos()  # actualizar despues

                if event.key == pygame.K_m:  # mata tanque en el indice 0
                    self.mapa.matar_tanque(0)

                if event.key == pygame.K_SPACE:
                    if self.turno_act < self.cantidad_human:
                        if (not self.mapa.tanques[self.turno_act].bala.disparado  # tiene bala en el aire
                                and self.mapa.tanques[self.turno_act].tiene_balas())\
                                and pygame.time.get_ticks() - self.ultimo_tiro > 500\
                                and self.mapa.tanques[self.turno_act].vivo():

                            self.mapa.tanques[self.turno_act].disparar()

                if event.key == pygame.K_1:
                    if self.turno_act < self.cantidad_human:
                        if not self.mapa.tanques[self.turno_act].bala.disparado:
                            self.mapa.tanques[self.turno_act].bala = Bala()
                            self.bala1Sound.play()

                if event.key == pygame.K_2:
                    if self.turno_act < self.cantidad_human:
                        if not self.mapa.tanques[self.turno_act].bala.disparado:
                            self.mapa.tanques[self.turno_act].bala = Bala("perforante")
                            self.bala2Sound.play()

                if event.key == pygame.K_3:
                    if self.turno_act < self.cantidad_human:
                        if not self.mapa.tanques[self.turno_act].bala.disparado:
                            self.mapa.tanques[self.turno_act].bala = Bala("105mm")
                            self.bala3Sound.play()

                # mover tanque 1
                # angulo

                if event.key == pygame.K_LEFT:
                    if self.turno_act < self.cantidad_human:
                        if not self.mapa.tanques[self.turno_act].bala.disparado:
                            self.mapa.tanques[self.turno_act].izq_apretar()

                if event.key == pygame.K_RIGHT:
                    if self.turno_act < self.cantidad_human:
                        if not self.mapa.tanques[self.turno_act].bala.disparado:
                            self.mapa.tanques[self.turno_act].der_apretar()

                # potencia
                if event.key == pygame.K_UP:
                    if self.turno_act < self.cantidad_human:
                        if not self.mapa.tanques[self.turno_act].bala.disparado:
                            self.mapa.tanques[self.turno_act].up_apretar()

                if event.key == pygame.K_DOWN:
                    if self.turno_act < self.cantidad_human:
                        if not self.mapa.tanques[self.turno_act].bala.disparado:
                            self.mapa.tanques[self.turno_act].down_apretar()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    if self.turno_act < self.cantidad_human:
                        if not self.mapa.tanques[self.turno_act].bala.disparado:
                            self.mapa.tanques[self.turno_act].izq_soltar()

                if event.key == pygame.K_RIGHT:
                    if self.turno_act < self.cantidad_human:
                        if not self.mapa.tanques[self.turno_act].bala.disparado:
                            self.mapa.tanques[self.turno_act].der_soltar()

                # potencia
                if event.key == pygame.K_UP:
                    if self.turno_act < self.cantidad_human:
                        if not self.mapa.tanques[self.turno_act].bala.disparado:
                            self.mapa.tanques[self.turno_act].up_soltar()

                if event.key == pygame.K_DOWN:
                    if self.turno_act < self.cantidad_human:
                        if not self.mapa.tanques[self.turno_act].bala.disparado:
                            self.mapa.tanques[self.turno_act].down_soltar()

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

    def sig_turno(self):
        self.mapa.tanques[self.turno_act].Eparametros()  # borra info tank
        self.turnos.remove(self.turno_act)
        if len(self.turnos) == 0:
            self.turnos = IA_aleatoria.mezclar_lista(datos.cantidad_tankes)
        self.turno_act = self.turnos[0]
        if not self.mapa.tanques[self.turno_act].vivo():
            self.sig_turno()

        self.mapa.tanques[self.turno_act].Aparametros(self.display)  # muestra info nuevo tank
        self.triangulo.mover(self.mapa.tanques[self.turno_act].getPos())
        self.ultimo_tiro = pygame.time.get_ticks()
