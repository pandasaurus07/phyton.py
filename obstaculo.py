# Imports go at the top
from microbit import *
from MicroRover import *

robot = Micro_Rover()

robot.move_forward(3)
robot.girarDerecha()
robot.move_forward(1)
robot.girarIzquierda()
robot.move_forward(5)
