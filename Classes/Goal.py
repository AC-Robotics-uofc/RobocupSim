
import pygame
from Classes.Ball import Ball # you can also import *
from Classes.Globals import *
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

    def scoreGoal(self, ball: Ball) -> bool:
        # if goal is on the left
        if self.xpos < 400:
            # if inside the net
            # ball is on the left side of the net   AND ball is below the top of the net   AND ball is also above the bottom of the net
            if (ball.xpos <= self.xpos + self.width) and (ball.ypos > self.ypos and ball.ypos < self.ypos + self.height): 
                # if ball is going towards the net
                # idk if it should be less than or EQUAL to but why not
                if ball.getXSpeed() <= 0:
                    score [1] +=1
                    ball.resetToMiddle()
                    ball.setSpeed([0,0])
                    return True

                
        # if goal is on the right
        else:
           
            # if inside the net
            # if ball is on the right side of the net AND ball is below the top of the net   AND ball is also above the bottom of the net
            if (ball.xpos >= self.xpos) and  (ball.ypos > self.ypos and ball.ypos < self.ypos + self.height):
                # idk if it should be greater than or EQUAL to but why not
                if ball.getXSpeed() >= 0:
                    score [0] +=1
                    ball.resetToMiddle()
                    ball.setSpeed([0,0])
                    return True
        return False
                    


    
    
    
    
