import pygame
import datos


class Menu():

    def __init__(self, game):  # Se entrega comoa arg game para poder ocupar las funciones construidas
        self.game = game  # Da acceso a variables de "game"
        self.mid_w, self.mid_h = self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2
        self.run_display = True  # Permite que siga corriendo el menú
        self.cursor_rect = pygame.Rect(0, 0, 20, 20)  # Ancho, Alto, X,Y
        self.offset = - 100  # Para que el indicador de menú quede alado izq del texto

    def draw_cursor(self):
        self.game.dibuja_texto('*', 15, self.cursor_rect.x, self.cursor_rect.y)  # Dibuja y ubica el indicador

    def blit_screen(self): #Updatea la pantalla
        self.game.window.blit(self.game.display, (0, 0))
        pygame.display.update()
        self.game.reset_keys()


class MainMenu(Menu): #Inicio clase menu principal, recibe como argumento la clase menu
    def __init__(self, game):

        Menu.__init__(self, game)
        self.state = 'Empieza Juego'
        self.startx, self.starty = self.mid_w, self.mid_h + 30
        self.controlsx, self.controlsy = self.mid_w, self.mid_h + 50
        self.creditsx, self.creditsy = self.mid_w, self.mid_h + 70
        self.cursor_rect.midtop = (self.startx + self.offset, self.starty)

    def display_menu(self):#Muestra menu
        self.run_display = True

        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill(datos.BLANCO)
            self.game.dibuja_texto('TANK SIMULATOR 2022', 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 20)
            self.game.dibuja_texto('Juego', 20, self.startx, self.starty)
            self.game.dibuja_texto('Controles', 20, self.controlsx, self.controlsy)
            self.game.dibuja_texto('Creditos', 20, self.creditsx, self.creditsy)
            self.draw_cursor()
            self.blit_screen()

    def move_cursor(self):

        if self.game.DOWN_KEY:  # Movimiento hacia abajo del cursor "#"
            if self.state == 'Empieza Juego':
                self.cursor_rect.midtop = (self.controlsx + self.offset, self.controlsy)
                self.state = 'Controles'
            elif self.state == 'Controles':
                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
                self.state = 'Creditos'
            elif self.state == 'Creditos':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = 'Empieza Juego'

        if self.game.UP_KEY:  # Movimiento hacia arriba del cursor "#"
            if self.state == 'Empieza Juego':
                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
                self.state = 'Creditos'
            elif self.state == 'Controles':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = 'Empieza Juego'
            elif self.state == 'Creditos':
                self.cursor_rect.midtop = (self.controlsx + self.offset, self.controlsy)
                self.state = 'Controles'

    def check_input(self):

        self.move_cursor()

        if self.game.START_KEY:

            if self.state == 'Empieza Juego':
                self.game.playing = True

            elif self.state == 'Controles':
                self.game.curr_menu = self.game.controls

            elif self.state == 'Creditos':
                self.game.curr_menu = self.game.credits

            self.run_display = False


class MenuControles(Menu):

    def __init__(self, game): #Definicion
        Menu.__init__(self, game)

    def display_menu(self):#Muestra menu de controles
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            if self.game.START_KEY or self.game.BACK_KEY:
                self.game.curr_menu = self.game.main_menu
                self.run_display = False
            self.game.display.fill(datos.BLANCO)
            self.game.dibuja_texto('CONTROLES', 45, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 280)
            self.game.dibuja_texto('numero 1 * bala 60mm', 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 200)
            self.game.dibuja_texto('numero 2 * bala perforante', 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 170)
            self.game.dibuja_texto('numero 3 * bala 105mm', 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 140)
            self.game.dibuja_texto('tecla izquierda  * rotar izquierda', 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 60)
            self.game.dibuja_texto('tecla derecha  * rotar derecha', 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 30)
            self.game.dibuja_texto('tecla arriba * aumentar potencia', 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 )
            self.game.dibuja_texto('tecla abajo * dismunuir potencia ', 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 30)
            self.game.dibuja_texto('barra espaciadora * disparar', 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 60)
            self.game.dibuja_texto('Boton Reset * Vuelve menu principal', 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 90)

            self.blit_screen()


class MenuCreditos(Menu):  # Creación clase menu de creditos.
    def __init__(self, game): #Definicion
        Menu.__init__(self, game)

    def display_menu(self):#Muestra menu de creditos
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
