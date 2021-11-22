from Tank import Tank


class Drawer:
    def __init__(self,tanques,pantalla):  # Fixme Creo que no funciona
        self.tanklist = tanques
        self.pantalla = pantalla

    def dibujar(self):
        for i in self.tanklist:
            i.sprites.draw(self.pantalla)



