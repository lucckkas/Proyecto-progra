from Tank import Tank


class Drawer:
    def __init__(self,tanques,pantalla):
        self.tanklist = tanques
        self.pantalla = pantalla

    def dibujar(self):
        for i in self.tanklist:
            i.sprites.draw(self.pantalla)



