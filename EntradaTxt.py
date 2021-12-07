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

    def dibujar(self, display):
        if self.activado:
            self.image.fill(datos.NEGRO)
            texto = self.letra.render(self.txt, True, datos.BLANCO)
        else:
            self.image.fill(datos.GRIS)
            texto = self.letra.render(self.txt, True, datos.GRIS2)
        display.blit(self.image, self.pos)
        display.blit(texto, [self.pos[0]+10, self.pos[1]+10])

    def comprueba_click(self, posicion_mouse):
        if self.pos[0] <= posicion_mouse[0] <= self.pos[0]+85 \
                and self.pos[1] <= posicion_mouse[1] <= self.pos[1]+40:
            self.activado = True
            menu.Menu.insertando = True

        else:
            self.activado = False
            menu.Menu.insertando = False

    def agrega_texto(self, event):
        if self.activado and (48 <= event.key <= 57 or 1073741913 <= event.key <= 1073741923 or event.key == 46):
            self.txt += event.unicode
        elif self.activado and event.key == 8:  # borrar
            self.txt = self.txt[:-1]
        elif self.activado and event.key == 13:  # enter
            if False:  # TODO comprobar que la entrada sea correcta (quiza deberia recibir la variable a ingresar)
                pass
            else:
                self.activado = False
                menu.Menu.insertando = False
