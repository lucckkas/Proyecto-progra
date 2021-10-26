import random as r


class IA_aleatoria():
    def __init__(self):
        self.angulo = 0
        self.potencia = 0

    def disparar(self):
        self.angulo = r.randint(10, 170)
        while 85 < self.angulo < 95:
            self.angulo = r.randint(10, 170)
        self.potencia = r.randint(40, 100)
        return [self.angulo, self.potencia]
