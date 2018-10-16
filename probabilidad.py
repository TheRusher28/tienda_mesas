import random

"""
Este es el codigo que randomiza el descuento de tu compra.
"""

__author__ = "TheRusher28"
__copyright__ = "Copyright 2018, TheRusher28"
__credits__ = "TheRusher28"

__mantainer__ = "TheRusher28"
__email__ = "therusher28@gmail.com"
__status__ = "Beginner"


balls = ["white ball", "red ball", "blue ball", "green ball", "yellow ball"]
choosen_ball = random.choice(balls)


def coger_bola(choosen_ball, precio_base):
    if choosen_ball == "white ball":
        print("Tienes 10% de descuento")
        precio_descuento = 90 * precio_base / 100
    elif choosen_ball == "red ball":
        print("Tienes 20% de descuento")
        precio_descuento = 80 * precio_base / 100
    elif choosen_ball == "blue ball":
        print("Tienes 30% de descuento")
        precio_descuento = 70 * precio_base / 100
    elif choosen_ball == "green ball":
        print("Tienes 40% de descuento")
        precio_descuento = 60 * precio_base / 100
    else:
        print("Tienes 50% de descuento")
        precio_descuento = 50 * precio_base / 100
    return precio_descuento
