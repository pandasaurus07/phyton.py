# Imports go at the top
from microbit import *
from maqueen import *

robot = Maqueen()



while True:
    distancia=robot.read_distance()
    if(distancia<10):
        robot.set_motor(1, 0)
        robot.set_motor(0, 0)
    else:
        robot.set_motor(1, 255)
        robot.set_motor(0, 255)
