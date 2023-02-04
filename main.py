import math
import pygame
import numpy
from Classes.PicObj import PicObj # you can also import *
from Classes.Robot import Robot # you can also import *
from Classes.Goal import Goal # you can also import *
from Classes.Ball import Ball # you can also import *
from Classes.Globals import * # to import all global variables




# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

if __name__ == '__main__':
    SPEED = 5
    RADIUS = 20
    GOALWIDTH = 30
    GOALHEIGHT = 100

    robot_list = []
    gameObjs = []
    ball = Ball(400, 400)
    redGoal = Goal(100, 400,GOALWIDTH,GOALHEIGHT,"red",RED)
    blueGoal = Goal(700, 400,GOALWIDTH,GOALHEIGHT,"blue", BLUE)

    run = True
    moving = False
    robot1 = Robot(SPEED, 10, 500,300, RED, RADIUS)
    robot2 = Robot(SPEED, 1, 100,500, RED, RADIUS)
    robot3 = Robot(SPEED, 10, 200,200, RED, RADIUS)
    #robotv2 = Robot2([50,50], [10,10,5])
    robot_list.append(robot1)
    robot_list.append(robot2)
    robot_list.append(robot3)

    gameObjs.append(ball)
    gameObjs.append(redGoal)
    gameObjs.append(blueGoal)
    gameObjs.append(robot1)
    gameObjs.append(robot2)
    gameObjs.append(robot3)

    while run:
        draw(WIN, gameObjs)
        #this works
        # if robot.xpos>0 and robot.ypos>0:
        #     robot.upLeft()

        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                moving = True
                if event.key == pygame.K_f:
                    print(get_distance(robot1, robot2))

            #     elif event.key == pygame.K_s:
            #         robot.down()
            #
            #     if event.key == pygame.K_a:
            #         robot.left()
            #     elif event.key == pygame.K_d:
            #         robot.right()
            control(robot1, event, ball)
        if not robot1.hasball and (ball.getSpeed()[0] != 0):
            if WIDTH>ball.xpos+ball.radius and ball.xpos-ball.radius>0 and HEIGHT>ball.ypos+ball.radius and ball.ypos-ball.radius>0:
                ball.move()
            else:#get it to bounce off walls
                ball.setSpeed([0,0])
        algorithm(robot2, robot3,ball, blueGoal)



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
