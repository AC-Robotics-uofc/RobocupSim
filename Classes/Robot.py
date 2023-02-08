import pygame
import math
from Classes.Globals import * # to import all global variables
class Robot:
    def __init__(self, speed,turn_speed, xpos, ypos, color,radius, directions):
        self.turn_speed = turn_speed #deg per frame
        self.xpos = xpos
        self.ypos = ypos
        #The amoun tof pixels moved in what we will say one sec
        self.speed = speed
        self.color = color
        #maybe make this static
        self.radius = radius
        self.hasball = False
        self.accel = 1
        self.front = [xpos,ypos+radius, 0]#initially looks down at 0 deg
        self.power = 0
        self.directions = directions
    
    def get_turn_speed(self):
        return self.turn_speed
    def up(self):
        self.ypos = self.ypos-self.speed
        self.updateFront()

    def down(self):
        self.ypos = self.ypos+self.speed
        self.updateFront()

    def right(self):
        self.xpos = self.xpos+self.speed
        self.updateFront()

    def left(self):
        self.xpos = self.xpos-self.speed
        self.updateFront()
    def foreward(self):
        self.xpos = self.xpos + self.speed*math.sin(math.radians(self.front[2]))
        self.ypos = self.ypos+ self.speed*math.cos(math.radians(self.front[2]))
        self.updateFront()

    def backward(self):
        self.xpos = self.xpos - self.speed*math.sin(math.radians(self.front[2]))
        self.ypos = self.ypos- self.speed*math.cos(math.radians(self.front[2]))
        self.updateFront()
    def turnRight(self):
        self.front[2] -=self.turn_speed
        if self.front[2] <0:
            self.front[2] = 360-self.turn_speed
        self.updateFront()
    def turnLeft(self):
        self.front[2] +=self.turn_speed
        if self.front[2] >360:
            self.front[2] = 0+ self.turn_speed
        self.updateFront()
    def getFront(self):
        return self.front
    def updateFront(self):
        self.front[0] = self.xpos + self.radius*math.sin(math.radians(self.front[2]))
        self.front[1]= self.ypos +self.radius*math.cos(math.radians(self.front[2]))
    def grabBall(self,ball):
        self.hasball = True
        self.ball = ball
    def getDegree(self):
        return self.front[2]
    def throwBall(self):
        if self.hasBall():
            self.hasball =False
            self.ball.setSpeed([self.speed, self.front[2]])


    def hasBall(self):
        return self.hasball


    def draw(self, win):
        pygame.draw.circle(win, self.color,(self.xpos,self.ypos), self.radius)
        pygame.draw.rect(win, self.color, (self.front[0]-5, self.front[1]-5, 10,10))

        #try give claw to indicate front
        #Spygame.draw.rect(win, self.color,())

    def control(robot, event, ball): # control checks which keys are pressed and updates the robot's movement booleans
        # 0 forward
        # 1 backward
        # 2 left
        # 3 right
        # 4 turn left
        # 5 turn right
        # 6 up
        # 7 down
        # F and B are respective to the front of the robot, while all others are headless
     if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_f:
                    robot.directions[0] = True
                elif event.key == pygame.K_b:
                    robot.directions[1] = True
                if event.key == pygame.K_a:
                    robot.directions[2] = True
                elif event.key == pygame.K_d:
                    robot.directions[3] = True
                if event.key == pygame.K_z:
                    robot.directions[4] = True
                elif event.key == pygame.K_x:
                    robot.directions[5] = True
                if event.key == pygame.K_w:
                    robot.directions[6] = True
                elif event.key == pygame.K_s:
                    robot.directions[7] = True
     if event.type == pygame.KEYUP:
                if event.key == pygame.K_f:
                    robot.directions[0] = False
                elif event.key == pygame.K_b:
                    robot.directions[1] = False
                if event.key == pygame.K_a:
                    robot.directions[2] = False
                elif event.key == pygame.K_d:
                    robot.directions[3] = False
                if event.key == pygame.K_z:
                    robot.directions[4] = False
                elif event.key == pygame.K_x:
                    robot.directions[5] = False
                if event.key == pygame.K_w:
                    robot.directions[6] = False
                elif event.key == pygame.K_s:
                    robot.directions[7] = False
    def drive(robot):
        if (robot.directions[0] == True):
            robot.foreward()
        if (robot.directions[1] == True):
            robot.backward()
        if (robot.directions[2] == True):
            robot.left()
        if (robot.directions[3] == True):
            robot.right()
        if (robot.directions[4] == True):
            robot.turnLeft()
        if (robot.directions[5] == True):
            robot.turnRight()
        if (robot.directions[6] == True):
            robot.up()
        if (robot.directions[7] == True):
            robot.down()
        

    def __lt__(self, other):
        return False

    