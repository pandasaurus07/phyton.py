# Imports go at the top
from microbit import *
from mcqueen import *

robot = Maqueen()

robot.set_motor(1, 100)
robot.set_motor(0, 100)
sleep(5000)
robot.set_motor(1, 0)
robot.set_motor(0, 0)
