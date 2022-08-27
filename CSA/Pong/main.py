

import pygame
import sys
sys.path.append("\\Users\\tom\\Desktop\\CSA")
from Pong.data.prepare import *
from Pong.data.game_objects import *
from Pong.data.game_controller import Controller
pygame.init()


p1 = Paddle(speed_player)


ball = Ball()
controller = Controller()
controller.set_objects(ball, p1)

while True:
    controller.check_events()
    controller.draw_screen()
    controller.update()
