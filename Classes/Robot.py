import pygame
import math
class Robot:
    def __init__(self, speed,turn_speed, xpos, ypos, color,radius):
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

    def __lt__(self, other):
        return False
