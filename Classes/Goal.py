
import pygame
class Goal:
    def __init__(self, xpos, ypos, width, height, team, color):
        self.xpos = xpos-(width/2)
        self.ypos = ypos-(height/2)
        self.team = team
        self.color = color
        self.width = width
        self.height = height

    def draw(self,win):
        #not tested
        pygame.draw.rect(win, self.color, (self.xpos, self.ypos, self.width,self.height))