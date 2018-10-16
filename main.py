#!/usr/bin/python3
import random
import datetime
from probabilidad import coger_bola
from probabilidad import choosen_ball

"""
Este codigo se aplicaria a una tienda de muebles, en la cual sus muebles tienen un precio base de 400€ y en base a 
la calidad de la madera y el numero de patas que tiene se determina si es de una gama o de otra y su precio.
0/3 == gama baja y el precio baja 101,1€ 
3/7 == gama media y no recibe ningun cambio en su precio
7/10 == gama alta y el precio sube 99,9€
"""

__author__ = "TheRusher28"
__copyright__ = "Copyright 2018, TheRusher28"
__credits__ = "TheRusher28"

__mantainer__ = "TheRusher28"
__email__ = "therusher28@gmail.com"
__status__ = "Beginner"

class Mueble:
    def __init__(self, altura, anchura, profundidad, peso, material, color, fecha_fabr, n_patas, n_cajones):
        self.altura = altura
        self.anchura = anchura
        self.profundidad = profundidad
        self.peso = peso
        self.gama = 'patata'
        self.material = material
        self.color = color
        self.estado = 100
        self.n_serie = random.randrange(100, 10000)
        self.fecha_fabr = fecha_fabr
        self.n_patas = n_patas
        self.n_cajones = n_cajones
        self.precio_base = 400
        self.puntos = 0

    def calcular_puntos_gama(self):
        """Calcula los puntos, para averiguar de que gama es nuestra mesa"""
        if self.material == 'madera barata':
            self.puntos += 1
            print('Tienes madera barata')
        if self.material == 'madera pino':
            self.puntos += 3
            print('Tienes madera de pino')
        if self.material == 'madera buena':
            self.puntos += 2
            print('Tienes madera buena')
        if self.n_patas == 4:
            self.puntos += 1
            print('Tienes 4 patas')
        if self.n_patas >= 8:
            self.puntos += 3
            print('Tienes 8 patas o mas')
        if self.n_patas == 6:
            self.puntos += 2
            print('Tienes 6 patas')
        if self.n_cajones == 0:
            self.puntos += 1
            print('tienes 0 cajones')
        if self.n_cajones > 0 and self.n_cajones <= 2:
            self.puntos += 2
            print('tienes entre 0 y 2 cajones')
        if self.n_cajones > 3:
            self.puntos += 3
            print('tienes 3 cajones o mas')

        #Aqui para de calcular puntos y empieza a calcular la gama.
        if self.puntos >= 0 and self.puntos <= 3:
            self.gama = 'gama baja'
        if self.puntos > 3 and self.puntos <= 7:
            self.gama = 'gama media'
        if self.puntos > 7:
            self.gama = 'gama alta'
        return self.gama

    def calcular_precio(self):
        """Calcula el precio total de nuestro producto, sumandole la variacion de gama"""
        if self.material == 'madera barata':
            self.precio_base -= 200
        if self.material == 'madera pino':
            self.precio_base += 200
        if self.n_patas == 4:
            self.precio_base -= 50
        if self.n_patas >= 8:
            self.precio_base += 50
        if self.n_cajones >= 0 and self.n_cajones <= 2:
            self.precio_base += 50
        if self.n_cajones >= 3:
            self.precio_base += 100

        if self.gama == 'gama baja':
            self.precio_base -= 101.1
        if self.gama == 'gama alta':
            self.precio_base += 99.9
        return self.precio_base

    def retornar_precio(self):
        """Metodo con el que puedo hacer que la variable self.precio_base se pueda trasladar a precio_base y poder ser usada en coger_bola()"""
        precio_base = self.precio_base
        return precio_base

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
mesa = Mueble(30, 20, 20, 10, 'madera barata', 'azul', '09/10/2018', 8, 4)   #Creando objeto mesa

print('Tu mesa es de gama: ', mesa.calcular_puntos_gama())      #Llamando a calcular_puntos_gama()
print('Precio: ', mesa.calcular_precio(), '€')       #Llamando a calcular_precio()

#cama = Cama(30, 20, 20, 10, 'madera pino', 'azul', '09/10/2018', 8, 0) (Ideas desechadas)
#print(cama.calcular_precio_cama(colchon))  (Ideas desechadas)

precio_base = mesa.retornar_precio()    #Asignando el valor que retorna retornar_precio() a precio_base

hoy = datetime.datetime.now()
navidad = datetime.datetime(year=2018, month=12, day=25)
black_friday = datetime.datetime(year=2018, month=11, day=23)
reyes_magos = datetime.datetime(year=2018, month=1, day=6)

def control_fecha(hoy, navidad, black_friday):
    if hoy.day == navidad.day and hoy.month == navidad.month:
        print(coger_bola(choosen_ball, precio_base))
    elif hoy.day == black_friday.day and hoy.month == black_friday.month:
        print(coger_bola(choosen_ball, precio_base))
    elif hoy.day == reyes_magos.day and hoy.month == reyes_magos.month:
        print(coger_bola(choosen_ball, precio_base))
    else:
        print("Hoy no hay promocion")
control_fecha(hoy, navidad, black_friday)
print(__copyright__)