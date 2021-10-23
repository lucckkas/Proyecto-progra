import Tank
import datos
import random as r


class IAtank(Tank.Tank):
    def __init__(self, pos):
        self.pos_ult = [0, 0]
        self.angle = r.randint(10, 170)
        while 85 < self.angulo < 95:
            self.angle = r.randint(10, 170)
        self.potencia = r.randint(40, 100)

    def disparar(self):

        return self.angle, self.potencia

    def update(self, pos):
        self.pos_ult = pos

