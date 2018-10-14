import random
import datetime
balls = ["white ball", "red ball", "blue ball", "green ball", "yellow ball"]
choosen_ball = random.choice(balls)
hoy = datetime.datetime(year=2018, month=12, day=25, hour=0, minute=0)
navidad = datetime.datetime(year=2018, month=12, day=25, hour=0, minute=0)
black_friday = datetime.datetime(year=2018, month=11, day=23, hour=0, minute=0)

def coger_bola(choosen_ball, precio_base):
    if choosen_ball == "white ball":
        print("Tienes 10% de descuento")
        precio_descuento = 10 * precio_base / 100
    elif choosen_ball == "red ball":
        print("Tienes 20% de descuento")
        precio_descuento = 20 * precio_base / 100
    elif choosen_ball == "blue ball":
        print("Tienes 30% de descuento")
        precio_descuento = 30 * precio_base / 100
    elif choosen_ball == "green ball":
        print("Tienes 40% de descuento")
        precio_descuento = 40 * precio_base / 100
    else:
        print("Tienes 50% de descuento")
        precio_descuento = 50 * precio_base / 100
        
def control_fecha(hoy, navidad, black_friday):
    if hoy == navidad:
        coger_bola(choosen_ball, precio_base)
    elif hoy == black_friday:
        coger_bola(choosen_ball, precio_base)
    else:
        print("Hoy no hay promocion")