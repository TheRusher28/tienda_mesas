import random
"""
0/25 == gama baja
25/50 == gama media
> 50 == gama alta
NO ESTA ACABADO, ESTA EN PROCESO
"""
class Mueble:
    def __init__(self, altura, anchura, profundidad, peso, gama, material, color, fecha_fabr, n_patas, n_cajones, puntos):
        self.altura = altura
        self.anchura = anchura
        self.profundidad = profundidad
        self.peso = peso
        self.gama = 'gama media'
        self.material = material
        self.color = color
        self.estado = 100
        self.n_serie = random.randrange(100, 10000)
        self.fecha_fabr = fecha_fabr
        self.n_patas = n_patas
        self.n_cajones = n_cajones
        self.precio_base = 1000
        self.puntos = puntos
    @property
    def calcular_precio(self):
        if self.material == 'madera_barata':
            self.precio_base -= 500
            self.puntos = 0
        if self.material == 'madera_pino':
            self.precio_base += 500
            self.puntos += 30
        if self.material == 'madera_buena':
            self.puntos += 15
        if self.n_patas == 4:
            self.precio_base -= 100
            self.puntos += 10
        if self.n_patas >= 8:
            self.precio_base += 100
            self.puntos += 20
        if self.n_patas >= 4 and self.n_patas <= 8:
            self.puntos += 15

        def calcular_gama(self):
            if self.puntos >= 0 and self.puntos <= 25:
                self.precio_base -= 100.1
                self.gama = 'gama baja'
            if self.puntos >= 25 and self.puntos <= 50:
                self.gama = 'gama media'
            if self.puntos >50:
                self.gama = 'gama alta'
            return self.gama

class Mesa(Mueble):
