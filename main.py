import math

import pygame
import numpy
#division A feild: 13.4m by 10.4m ratio = 1.288 with play area of 12 by 9 and 1,333 ratio
HEIGHT = 800
WIDTH = HEIGHT*1.288
PIXCON= 10.4/HEIGHT

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Robocup Sim")

RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
WHITE = (255,255,255)
BLACK = (0,0,0)#10 diff shades
PURPLE = (120,0,120)
ORANGE = (255,165, 0)
GREY = (128,128,128)
TURQUOISE = (64,224,208)

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
class PicObj:
    def __init__(self, pos):
        self.pos = pos
        
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
        return self.v

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def get_distance(robot1, robot2):
    return math.hypot(abs(robot2.xpos-robot1.xpos), abs(robot2.ypos-robot1.ypos))

def getBallDist(robot, ball):
    front = robot.getFront()
    return math.hypot(abs(ball.xpos-front[0]), abs(ball.ypos-front[1]))
def getRBD(robot, ball):#robot ball degree
    deg = 0
    front = robot.getFront()
    yDiff = front[1]-ball.ypos
    xDiff = front[0]-ball.xpos
    if xDiff<0 and yDiff>0:
        deg = 90
    elif xDiff<0 and yDiff<0:
        deg = 180
    elif xDiff>0 and yDiff<0:
        deg = 270

    return round(math.degrees(math.atan(abs(yDiff)/abs(xDiff))))+deg
# Press the green button in the gutter to run the script.
def draw_robots(win, robot_list):
    for robot in robot_list:
        robot.draw(win)
def draw(win, robot_list):
    win.fill(WHITE)
    draw_robots(win, robot_list)
    pygame.display.update()
def updateBall(robot, ball):

    if robot.hasball:
        front = robot.getFront()
        ball.xpos = front[0]
        ball.ypos = front[1]

def setDeg(robot, deg):
    if robot.front[2]> deg:
        robot.turnRight()
    elif robot.front[2]< deg:
        robot.turnLeft()


def algorithm(robot2, robot3, ball, goal):
    dist = getBallDist(robot2, ball)
    setDeg(robot2, getRBD(robot2, ball))
    if (dist>0 and getRBD(robot2, ball)+1>=robot2.getDegree()>=getRBD(robot2, ball)-1):
        robot2.foreward()
    if 5>dist:
        robot2.grabBall(ball)
    if robot2.hasball:
        setDeg(robot2, getRBD(robot2, goal))
        if getRBD(robot2, goal)+1>=robot2.getDegree()>=getRBD(robot2, goal)-1:
            robot2.throwBall()
    
def control(robot, event, ball):
     if event.type == pygame.TEXTINPUT:
                if event.text =="w":
                    robot.up()
                elif event.text == "s":
                    robot.down()

                if event.text == "a":
                    robot.left()
                elif event.text == "d":
                    robot.right()
                if event.text == "q":
                    robot.turnLeft()
                    print(getBallDist(robot, ball))
                elif event.text == "e":
                    robot.turnRight()
                if event.text == "r":
                    robot.foreward()
                if event.text == "z":
                    if getBallDist(robot, ball)< 5:
                        robot.grabBall(ball)
                elif event.text == "x":
                    robot.throwBall()
                updateBall(robot, ball)
                #print(robot.front[2])



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
