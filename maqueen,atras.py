# Imports go at the top
from microbit import *
from maqueen import *

robot = Maqueen()



while True:

        robot.set_motor(1, -255)
        robot.set_motor(0, -255)
