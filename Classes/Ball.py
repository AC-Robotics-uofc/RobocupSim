import math
import pygame
from Classes.Globals import *

class Ball:
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
        self.inGoal = False
        self.color = BLACK
        self.radius = 10
        self.v = [0,0]

    def draw(self, win):
        pygame.draw.circle(win, self.color,(self.xpos,self.ypos), self.radius)

    def move(self):
        #feel like doing wrong
        self.xpos = self.xpos+ self.v[0]*math.sin(math.radians(self.v[1]))
        self.ypos = self.ypos+ self.v[0]*math.cos(math.radians(self.v[1]))

    def setSpeed(self,v):
        self.v = v

    
    def getSpeed(self):
        """Returns the speed of the ball as a list, index 0 is the velocity of the ball while index 1 is the direction of the ball (in degrees).
            \nIf you want the velocity in one direction make sure you use math.sin or math.cos.\nTo get the x speed use math.sin, its weird but its correct"""
        return self.v
    
    def getXSpeed(self):
        return self.v[0]*math.sin(math.radians(self.v[1]))
    
    def getYSpeed(self):
        return self.v[0]*math.cos(math.radians(self.v[1]))
    
    def resetToMiddle(self):
        self.xpos = HEIGHT /2
        self.ypos = WIDTH /2

