# -*- coding: utf-8 -*-
import pygame
import math
import datos


def trans_ang_rad(ang):  # cambia angulos de grados a radianes
    return ang * math.pi / 180


def trans_ang_grad(ang):  # cambia angulos de radianes a grados
    return ang * 180 / math.pi


class Bala(pygame.sprite.Sprite):
    def __init__(self, tipo_bala="60mm"):
        super().__init__()
        self.image = pygame.image.load(datos.abrir(datos.carpeta_balas, f"{tipo_bala}.png"))
        self.rect = self.image.get_rect()
        self.tipo = f"{tipo_bala}.png"  # ¿por que .png?
        self.velocidad_inicialV = 0
        self.velocidad_inicialH = 0
        self.disparado = False
        self.ang_act = 0
        self.temp = 0

        # guarda la imagen para no perder la calidad al rotar
        self.imagen_original = pygame.image.load(datos.abrir(datos.carpeta_balas, f"{tipo_bala}.png"))
        self.alturamaxima = 0
        self.tiempo = 0
        # las variables posX y posY son para calcular la posicion de la bala con flotantes
        self.posY = 0
        self.posX = 0

        self.posxInicio = 0

        self.coordinate = []  # aqui se guardan las posiciones donde ha estado la bala
        self.coord_time = pygame.time.get_ticks()  # para controlar cuando se guardan las posiciones

        if tipo_bala == "105mm":
            self.dagno = datos.dagno_105mm
            self.tam_explocion = datos.tam_exp_105mm

        if tipo_bala == "perforante":
            self.dagno = datos.dagno_perforante
            self.tam_explocion = datos.tam_exp_perforante

        if tipo_bala == "60mm":
            self.dagno = datos.dagno_60mm
            self.tam_explocion = datos.tam_exp_60mm

        # atributos de prueba explocion terreno
        self.puntos_x = []
        self.puntos_ypos = []
        self.puntos_yneg = []
        self.distancia_ypos_yneg = []

        self.Fpos_balaX = 0
        self.Fpos_balaY = 0

        ################################

    def disparar(self, angulo, potencia, posX, posY):  # coloca la bala y asigna su posicion y movimiento
        self.rect.center = (posX, posY)
        self.coordinate.clear()
        self.coord_time = pygame.time.get_ticks()
        self.posY = posY
        self.posX = posX
        self.posxInicio = posX
        self.ang_act = angulo
        self.velocidad_inicialV = math.sin(trans_ang_rad(angulo)) * potencia
        self.velocidad_inicialH = math.cos(trans_ang_rad(angulo)) * potencia
        self.disparado = True
        self.alturamaxima = (self.velocidad_inicialV * self.velocidad_inicialV) / (2 * datos.GRAVEDAD_TIERRA)
        self.temp = pygame.time.get_ticks()
        self.viento = datos.viento

    def rotar(self, surface, angulo):  # rota surface en angulo y la centra
        bala_rotada = pygame.transform.rotozoom(surface, angulo, 1)
        bala_rotada_pos = bala_rotada.get_rect(center=(self.rect.centerx, self.rect.centery))
        return bala_rotada, bala_rotada_pos

    def update(self):  # actualiza su posicion
        # validacion para facilitar las pruebas:
        """
        if self.rect.centery < TAMAGNO_MAPA[1] and self.rect.centerx > TAMAGNO_MAPA[0] and and self.rect.centerx < 0:
            self.detener()
        """
        if self.disparado:
            vel = pygame.time.get_ticks() - self.temp
            vel = vel/140  # esta variable representa el tiempo en las formulas de movimiento
            # fornulas posicion
            self.rect.centerx = self.posX + self.velocidad_inicialH * vel + 0.5 * self.viento/5 * vel * vel
            self.rect.centery = self.posY - self.velocidad_inicialV * vel + 0.5 * datos.GRAVEDAD_TIERRA * vel * vel

            # cada 50 ms guarda la posicion de la bala en coordinate
            tick = pygame.time.get_ticks()
            if tick - self.coord_time > 50:
                self.coordinate.append((self.rect.centerx, self.rect.centery))
                self.coord_time = pygame.time.get_ticks()

            # rotacion
            velocidad_horizontal_act = self.velocidad_inicialH + self.viento/5 * vel
            if velocidad_horizontal_act == 0:  # forma cutre de arreglar posible div por 0 XD
                velocidad_horizontal_act = 0.00000000001
            velocidad_vertical_act = self.velocidad_inicialV - datos.GRAVEDAD_TIERRA * vel
            if velocidad_horizontal_act < 0:  # si va hacia la izquierda
                self.ang_act = trans_ang_grad(math.atan((
                        velocidad_vertical_act /
                        velocidad_horizontal_act))) + 180
                bala_rotada, bala_rotada_pos = self.rotar(self.imagen_original, self.ang_act)
                self.image = bala_rotada
                self.rect = bala_rotada_pos
            else:
                self.ang_act = trans_ang_grad(math.atan((
                        velocidad_vertical_act /
                        velocidad_horizontal_act)))
                bala_rotada, bala_rotada_pos = self.rotar(self.imagen_original, self.ang_act)
                self.image = bala_rotada
                self.rect = bala_rotada_pos

    def detener(self):
        self.velocidad_inicialV = 0
        self.velocidad_inicialH = 0
        self.disparado = False
        self.kill()
        self.goto0_0()

    def explotar_terreno(self):
        self.Fpos_balaX = self.getPos_X()
        self.Fpos_balaY = self.getPos_Y()
        
        i = self.Fpos_balaX - (self.tam_explocion + 2)
        
        # generar los puntos X
        while i != self.Fpos_balaX + self.tam_explocion:
            
            add = i
            if add >= datos.tamagno_mapa[0]-1:
                add = datos.tamagno_mapa[0]-1

            if add <= 1:
                add = 1
            
            self.puntos_x.append(add)
            i = i+2
        
        # generar los puntos Y  positivos
        for i in self.puntos_x:
            y = ((self.tam_explocion ** 2) - (i-self.Fpos_balaX)**2)
            yabs = abs(y)
            ylisto = math.sqrt(yabs) + self.Fpos_balaY
            yredon = ylisto
                
            self.puntos_ypos.append(yredon)
        
        # generar puntos Y negativos
        for i in self.puntos_x:
            
            y = (self.tam_explocion ** 2) - (i - self.Fpos_balaX)**2
            yabs = abs(y)
            ylisto = -math.sqrt(yabs) + self.Fpos_balaY
            yredon = ylisto
            
            self.puntos_yneg.append(yredon)
        
        # generar lista con distancia y positiva y negativa
        for i in range(len(self.puntos_ypos)):
            dist = self.puntos_ypos[i] - self.puntos_yneg[i]
            
            self.distancia_ypos_yneg.append(dist)
    
    def reinicia_lista(self):
        self.puntos_yneg = []
        self.puntos_ypos = []
        self.puntos_x = []
        self.distancia_ypos_yneg = []
    
        # self.Fpos_balaX
        # self.Fpos_balaY

    # funciones que retornan valores:
    def get_altura(self):
        return self.alturamaxima

    def get_diametro(self):
        return self.tam_explocion*2

    def getPos(self):
        return self.rect.center

    def getPos_X(self):
        return self.rect.centerx

    def getPos_Y(self):
        return self.rect.centery

    def en_rad_exp(self, pos):
        compx = math.pow((self.getPos_X()-pos[0]), 2)
        compy = math.pow((self.getPos_Y()-pos[1]), 2)
        distancia = math.sqrt(compx + compy)
        if distancia <= self.tam_explocion + 15:
            return self.dagno*750/(distancia*distancia)
        return 0
    # mueve la bala al 200,0
    def goto0_0(self):
        self.rect.centerx = 200
        self.rect.centery = 0


# ciclo para pruebas DESACTUALIZADO
"""                                                                                 
pygame.init()
clock = pygame.time.Clock()

pantalla = pygame.display.set_mode(TAMAGNO_MAPA)
pygame.display.set_caption("preliminar")

balas = pygame.sprite.Group()
bala1 = Bala()
balas.add(bala1)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            bala1.disparar(85, 100 + 20, 20, 0)
        if event.type == pygame.KEYUP:
            bala1.detener()

    balas.update()
    pantalla.fill((180, 180, 180))
    balas.draw(pantalla)
    pygame.display.update()
    clock.tick(FPS)
"""
