import random as r

import datos


def mezclar_lista(njugadores):
    aux = []
    turnos = []
    datos.viento += r.randint(-3, 3)
    if datos.viento > 10:
        datos.viento = 10
    elif datos.viento < -10:
        datos.viento = -10

    for i in range(njugadores):
        aux.append(i)

    for i in range(len(aux)):
        nuevo_turno = r.randint(0, len(aux) - 1)

        turnos.append(aux[nuevo_turno])
        aux.remove(aux[nuevo_turno])

    return turnos


class IA_aleatoria:
    def __init__(self):
        self.angulo = 0
        self.potencia = 0

    def disparar(self):
        self.angulo = r.randint(10, 170)
        while 85 < self.angulo < 95:
            self.angulo = r.randint(10, 170)
        self.potencia = r.randint(40, 100)
        return [self.angulo, self.potencia]
