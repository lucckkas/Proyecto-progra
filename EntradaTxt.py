import pygame
import datos
import menu


class EntradaTxt:
    def __init__(self, pos, texto_defecto):
        self.pos = pos
        self.color_defecto = datos.GRIS
        self.activado = False
        self.letra = pygame.font.Font(None, 40)
        self.txt = str(texto_defecto)
        self.image = pygame.Surface((85, 40))
        if texto_defecto == datos.cantidad_tankes:
            self.tipo = 0
        elif texto_defecto == datos.cantidad_IA:
            self.tipo = 1
        elif texto_defecto == datos.GRAVEDAD_TIERRA:
            self.punto = True
            self.tipo = 2
        elif texto_defecto == datos.tamagno_mapa[0]:
            self.tipo = 3
        elif texto_defecto == datos.tamagno_mapa[1]:
            self.tipo = 4
        elif texto_defecto == datos.balas_60mm:
            self.tipo = 5
        elif texto_defecto == datos.balas_perforantes:
            self.tipo = 6
        elif texto_defecto == datos.balas_105mm:
            self.tipo = 7

    def dibujar(self, display):
        if self.activado:
            if self.valida():
                self.image.fill(datos.NEGRO)
            else:
                self.image.fill(datos.ROJO)
            texto = self.letra.render(self.txt, True, datos.BLANCO)
        else:
            self.image.fill(datos.GRIS)
            texto = self.letra.render(self.txt, True, datos.GRIS2)
        display.blit(self.image, self.pos)
        display.blit(texto, [self.pos[0]+10, self.pos[1]+10])

    def comprueba_click(self, posicion_mouse):
        if self.pos[0] <= posicion_mouse[0] <= self.pos[0]+85 \
                and self.pos[1] <= posicion_mouse[1] <= self.pos[1]+40 and not menu.Menu.insertando:
            self.activado = True
            menu.Menu.insertando = True

        else:
            if self.activado and len(self.txt) > 0 and self.valida():
                self.activado = False
                menu.Menu.insertando = False

    def valida(self):
        if len(self.txt) < 1:
            return False
        if self.tipo == 0:
            if 2 <= int(self.txt) <= 6:
                datos.cantidad_tankes = int(self.txt)
                return True
            return False
        elif self.tipo == 1:
            if 0 <= int(self.txt) <= 6 and int(self.txt) <= datos.cantidad_tankes:
                datos.cantidad_IA = int(self.txt)
                return True
            return False
        elif self.tipo == 2:
            if 1 <= float(self.txt) <= 20:
                datos.GRAVEDAD_TIERRA = float(self.txt)
                return True
            return False
        elif self.tipo == 3:
            if 800 <= int(self.txt) <= 1600:
                datos.tamagno_mapa[0] = int(self.txt)
                return True
            return False
        elif self.tipo == 4:
            if 800 <= int(self.txt) <= 1600:
                datos.tamagno_mapa[1] = int(self.txt)
                return True
            return False
        elif self.tipo == 5:
            if 0 <= int(self.txt) <= 30:
                datos.balas_60mm = int(self.txt)
                return True
            return False
        elif self.tipo == 6:
            if 0 <= int(self.txt) <= 100:
                datos.balas_perforantes = int(self.txt)
                return True
            return False
        elif self.tipo == 7:
            if 0 <= int(self.txt) <= 30:
                datos.balas_105mm = int(self.txt)
                return True
            return False

    def agrega_texto(self, event):
        if self.activado:
            if (48 <= event.key <= 57 or 1073741913 <= event.key <= 1073741922) and len(self.txt) < 4:
                self.txt += event.unicode
            elif self.tipo == 2 and (event.unicode == ".") and not self.punto:
                self.punto = True
                self.txt += event.unicode
            elif len(self.txt) > 0 and event.key == 8:  # borrar
                if self.txt[-1] == ".":
                    self.punto = False
                self.txt = self.txt[:-1]
            elif event.key == 13:  # enter
                if len(self.txt) > 0 and self.valida():
                    self.activado = False
                    menu.Menu.insertando = False
