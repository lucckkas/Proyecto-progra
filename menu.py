import pygame
import Checkbox
import datos
import EntradaTxt


class Menu:
    insertando = False

    def __init__(self, game):  # Se entrega comoa arg game para poder ocupar las funciones construidas
        self.game = game  # Da acceso a variables de "game"
        self.mid_w, self.mid_h = self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2
        self.run_display = True  # Permite que siga corriendo el menú
        self.cursor_rect = pygame.Rect(0, 0, 20, 20)  # Ancho, Alto, X,Y
        self.offset = - 100  # Para que el indicador de menú quede alado izq del texto
        self.clock = pygame.time.Clock()

    def blit_screen(self):  # Updatea la pantalla
        self.game.window.blit(self.game.display, (0, 0))
        pygame.display.update()
        self.game.reset_keys()
        self.clock.tick(datos.FPS)  # no creo que un menu necesite mas de 45 fps


class MainMenu(Menu):  # Inicio clase menu principal, recibe como argumento la clase menu
    def __init__(self, game):
        super().__init__(game)
        self.state = 'Empieza Juego'
        self.startx, self.starty = self.mid_w, self.mid_h + 30
        self.controlsx, self.controlsy = self.mid_w, self.mid_h + 50
        self.ajustesx, self.ajustesy = self.mid_w, self.mid_h + 70
        self.creditsx, self.creditsy = self.mid_w, self.mid_h + 150
        self.cursor_rect.midtop = (self.startx + self.offset, self.starty)

    def draw_cursor(self):
        self.game.dibuja_texto('*', 15, self.cursor_rect.x, self.cursor_rect.y)  # Dibuja y ubica el indicador

    def display_menu(self):  # Muestra menu
        self.run_display = True

        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill(datos.BLANCO)
            self.game.dibuja_texto('TANK SIMULATOR 2022', 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 20)
            self.game.dibuja_texto('Juego', 20, self.startx, self.starty)
            self.game.dibuja_texto('Controles', 20, self.controlsx, self.controlsy)
            self.game.dibuja_texto('Ajustes', 20, self.ajustesx, self.ajustesy)
            self.game.dibuja_texto('Creditos', 20, self.creditsx, self.creditsy)
            self.draw_cursor()
            self.blit_screen()

    def move_cursor(self):

        if self.game.DOWN_KEY:  # Movimiento hacia abajo del cursor "#"
            if self.state == 'Empieza Juego':
                self.cursor_rect.midtop = (self.controlsx + self.offset, self.controlsy)
                self.state = 'Controles'
            elif self.state == 'Controles':
                self.cursor_rect.midtop = (self.ajustesx + self.offset, self.ajustesy)
                self.state = 'Ajustes'
            elif self.state == 'Ajustes':
                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
                self.state = 'Creditos'
            elif self.state == 'Creditos':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = 'Empieza Juego'

        if self.game.UP_KEY:  # Movimiento hacia arriba del cursor "#"
            if self.state == 'Empieza Juego':
                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
                self.state = 'Creditos'
            elif self.state == 'Creditos':
                self.cursor_rect.midtop = (self.ajustesx + self.offset, self.ajustesy)
                self.state = 'Ajustes'
            elif self.state == 'Ajustes':
                self.cursor_rect.midtop = (self.controlsx + self.offset, self.controlsy)
                self.state = 'Controles'
            elif self.state == 'Controles':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = 'Empieza Juego'

    def check_input(self):

        self.move_cursor()

        if self.game.START_KEY:

            if self.state == 'Empieza Juego':
                self.game.playing = True

            elif self.state == 'Controles':
                self.game.curr_menu = self.game.controls

            elif self.state == 'Ajustes':
                self.game.curr_menu = self.game.ajustes

            elif self.state == 'Creditos':
                self.game.curr_menu = self.game.credits

            self.run_display = False


class MenuControles(Menu):

    def display_menu(self):  # Muestra menu de controles
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            if self.game.START_KEY or self.game.BACK_KEY:
                self.game.curr_menu = self.game.main_menu
                self.run_display = False
            self.game.display.fill(datos.BLANCO)
            self.game.dibuja_texto('CONTROLES', 45, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 280)
            self.game.dibuja_texto('numero 1 * bala 60mm', 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 200)
            self.game.dibuja_texto('numero 2 * bala perforante', 20, self.game.DISPLAY_W / 2,
                                   self.game.DISPLAY_H / 2 - 170)
            self.game.dibuja_texto('numero 3 * bala 105mm', 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 140)
            self.game.dibuja_texto('tecla izquierda  * rotar izquierda', 20, self.game.DISPLAY_W / 2,
                                   self.game.DISPLAY_H / 2 - 60)
            self.game.dibuja_texto('tecla derecha  * rotar derecha', 20, self.game.DISPLAY_W / 2,
                                   self.game.DISPLAY_H / 2 - 30)
            self.game.dibuja_texto('tecla arriba * aumentar potencia', 20, self.game.DISPLAY_W / 2,
                                   self.game.DISPLAY_H / 2)
            self.game.dibuja_texto('tecla abajo * dismunuir potencia ', 20, self.game.DISPLAY_W / 2,
                                   self.game.DISPLAY_H / 2 + 30)
            self.game.dibuja_texto('barra espaciadora * disparar', 20, self.game.DISPLAY_W / 2,
                                   self.game.DISPLAY_H / 2 + 60)
            self.game.dibuja_texto('Boton Reset * Vuelve menu principal', 20, self.game.DISPLAY_W / 2,
                                   self.game.DISPLAY_H / 2 + 90)

            self.blit_screen()


class MenuCreditos(Menu):  # Creación clase menu de creditos.

    def display_menu(self):  # Muestra menu de creditos
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            if self.game.START_KEY or self.game.BACK_KEY:
                self.game.curr_menu = self.game.main_menu
                self.run_display = False
            self.game.display.fill(datos.BLANCO)
            self.game.dibuja_texto('Hecho por', 45, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 120)
            self.game.dibuja_texto('Matias Camilla', 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 20)
            self.game.dibuja_texto('Jorge Migueles', 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 50)
            self.game.dibuja_texto('Gustavo Sanchez', 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 80)
            self.game.dibuja_texto('Luckas Strnad', 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 110)
            self.blit_screen()


class MenuAjustes(Menu):  # Creación clase menu de ajustes

    def __init__(self, game):
        super().__init__(game)
        self.cajas_texto = []
        self.cajas_texto.append(EntradaTxt.EntradaTxt([self.game.DISPLAY_W / 2 - 40, self.game.DISPLAY_H / 2 - 170], datos.cantidad_tankes, 0))
        self.cajas_texto.append(EntradaTxt.EntradaTxt([self.game.DISPLAY_W / 2 - 40, self.game.DISPLAY_H / 2 - 70], datos.cantidad_IA, 1))
        self.cajas_texto.append(EntradaTxt.EntradaTxt([self.game.DISPLAY_W / 2 - 140, self.game.DISPLAY_H / 2 + 30], datos.GRAVEDAD_TIERRA, 2))
        self.check = Checkbox.Checkbox([self.game.DISPLAY_W / 2 + 80, self.game.DISPLAY_H / 2 + 30])
        self.cajas_texto.append(EntradaTxt.EntradaTxt([self.game.DISPLAY_W / 2 - 110, self.game.DISPLAY_H / 2 + 130], datos.tamagno_mapa[0], 3))
        self.cajas_texto.append(EntradaTxt.EntradaTxt([self.game.DISPLAY_W / 2 + 30, self.game.DISPLAY_H / 2 + 130], datos.tamagno_mapa[1], 4))
        self.cajas_texto.append(EntradaTxt.EntradaTxt([self.game.DISPLAY_W / 2 - 190, self.game.DISPLAY_H / 2 + 230], datos.balas_60mm, 5))
        self.cajas_texto.append(EntradaTxt.EntradaTxt([self.game.DISPLAY_W / 2 - 40, self.game.DISPLAY_H / 2 + 230], datos.balas_perforantes, 6))
        self.cajas_texto.append(EntradaTxt.EntradaTxt([self.game.DISPLAY_W / 2 + 110, self.game.DISPLAY_H / 2 + 230], datos.balas_105mm, 7))

    def display_menu(self):  # Muestra menu de opciones

        self.run_display = True
        while self.run_display:
            self.game.check_events()
            if (self.game.START_KEY or self.game.BACK_KEY) and not Menu.insertando:
                datos.efecto_entorno = self.check.activado
                self.game.__init__()
                self.game.curr_menu = self.game.main_menu
                self.run_display = False

            self.game.display.fill(datos.BLANCO)

            self.game.dibuja_texto('AJUSTES', 45, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 280)
            self.game.dibuja_texto('CANTIDAD DE TANQUES', 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 200)
            self.game.dibuja_texto('CANTIDAD DE IA', 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 100)
            self.game.dibuja_texto('EFECTOS DE ENTORNOS', 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2)
            self.game.dibuja_texto('TAMAñO DEL MAPA', 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 100)
            self.game.dibuja_texto('X', 20, self.game.DISPLAY_W / 2 + 5, self.game.DISPLAY_H / 2 + 150)
            self.game.dibuja_texto('CANTIDAD DE BALAS', 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 200)

            #Descripción
            self.game.dibuja_texto('[ 2 a 6 ]', 12, self.game.DISPLAY_W / 2 + 90, self.game.DISPLAY_H / 2 - 150)
            self.game.dibuja_texto('Gravedad', 12, self.game.DISPLAY_W / 2 - 200, self.game.DISPLAY_H / 2 + 40)
            self.game.dibuja_texto('[ 1 a 20 ]', 12, self.game.DISPLAY_W / 2 - 200, self.game.DISPLAY_H / 2 + 55)
            self.game.dibuja_texto('Activar viento', 12, self.game.DISPLAY_W / 2 + 200, self.game.DISPLAY_H / 2 + 47)
            self.game.dibuja_texto('balas 60mm', 10, self.game.DISPLAY_W / 2 - 150, self.game.DISPLAY_H / 2 + 280)
            self.game.dibuja_texto('balas Perforantes', 10, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 280)
            self.game.dibuja_texto('balas 105mm', 10, self.game.DISPLAY_W / 2 + 150, self.game.DISPLAY_H / 2 + 280)

            self.check.dibujar(self.game.display)
            for i in self.cajas_texto:
                i.dibujar(self.game.display)
            self.blit_screen()
