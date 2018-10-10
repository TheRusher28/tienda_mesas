#!/usr/bin/python3
import random
import datetime
"""
Este codigo se aplicaria a una tienda de muebles, en la cual sus muebles tienen un precio base de 1000€ y en base a 
la calidad de la madera y el numero de patas que tiene se determina si es de una gama o de otra y su precio.
0/25 == gama baja y el precio baja 101,1€ 
25/50 == gama media y no recibe ningun cambio en su precio
> 50 == gama alta y el precio sube 99,9€
Cosas a añadir en el futuro: Añadir codigo posibilidad de descuento en caso de dia festivo
PD: Se que el proyecto tiene dos archivos que no tienen nada que ver, el archivo __init__.py 
contiene el codigo que la posibilidad de descuento en caso de dia festivo, pero todavia no 
esta aplicado a la tienda de muebles
"""

__author__ = "TheRusher28"
__copyright__ = "Copyright 2018, TheRusher28"
__credits__ = "TheRusher28"

__mantainer__ = "TheRusher28"
__email__ = "therusher28@gmail.com"
__status__ = "Beginner"

hoy = datetime.datetime.now()
navidad = datetime.datetime(year=2018, month=12, day=25, hour=0, minute=0)
black_friday = datetime.datetime(year=2018, month=11, day=23, hour=0, minute=0)

class Mueble:
    def __init__(self, altura, anchura, profundidad, peso, material, color, fecha_fabr, n_patas, n_cajones):
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
        self.puntos = 0

    def calcular_puntos_gama(self):
        """Calcula los puntos, para averiguar de que gama es nuestra mesa"""
        if self.material == 'madera_barata':
            self.puntos = 0
        if self.material == 'madera_pino':
            self.puntos += 30
        if self.material == 'madera_buena':
            self.puntos += 15
        if self.n_patas == 4:
            self.puntos += 10
        if self.n_patas >= 8:
            self.puntos += 20
        if self.n_patas >= 4 and self.n_patas <= 8:
            self.puntos += 15
        #Aqui para de calcular puntos y empieza a calcular la gama.
        if self.puntos >= 0 and self.puntos <= 25:
            self.gama = 'gama baja'
        if self.puntos >= 25 and self.puntos <= 50:
            self.gama = 'gama media'
        if self.puntos > 50:
            self.gama = 'gama alta'
        return self.gama

    def calcular_precio(self):
        """Calcula el precio total de nuestro producto, sumandole la variacion de gama"""
        if self.material == 'madera_barata':
            self.precio_base -= 500
        if self.material == 'madera_pino':
            self.precio_base += 500
        if self.n_patas == 4:
            self.precio_base -= 100
        if self.n_patas >= 8:
            self.precio_base += 100
        if self.gama == 'gama baja':
            self.precio_base -= 101.1
        if self.gama == 'gama media':
            self.precio_base += 99.9
        return self.precio_base

"""
Esto era una idea que tenia en mente pero la acabé dejando porque no sabia como añadir colchon como variable 
de la clase y a la vez usarlo el calcular_precio_cama()
class Cama(Mueble):
    self.colchon = input('¿Tiene su cama colchon? (S/N) ')
    def calcular_precio_cama(self, colchon):
        if self.material == 'madera_barata':
            self.precio_base -= 500
        if self.material == 'madera_pino':
            self.precio_base += 500
        if self.n_patas == 4:
            self.precio_base -= 100
        if self.n_patas >= 8:
            self.precio_base += 100
        if self.gama == 'gama baja':
            self.precio_base -= 101.1
        if self.gama == 'gama media':
            self.precio_base += 99.9
        if colchon == 'S':
            self.precio_base += 299.9

        return self.precio_base
"""
#(self, altura, anchura, profundidad, peso, material, color, fecha_fabr, n_patas, n_cajones):
mesa = Mueble(30, 20, 20, 10, 'madera pino', 'azul', '09/10/2018', 8, 12)
print(mesa.calcular_puntos_gama())
print(mesa.calcular_precio())
#cama = Cama(30, 20, 20, 10, 'madera pino', 'azul', '09/10/2018', 8, 0)
#print(cama.calcular_precio_cama(colchon))