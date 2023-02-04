import pygame
import math
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

score = [0, 0] # index 0 is red team and index 1 is blue team



# GLOBAL FUNCTIONS -----------------------------------------------------------------------------------------------------
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
    draw_score(win, score)
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
                if event.text =="r":
                    robot.up()
                elif event.text == "s":
                    robot.down()

                if event.text == "y":
                    robot.left()
                elif event.text == "t":
                    robot.right()
                if event.text == "a":
                    robot.turnLeft()
                    print(getBallDist(robot, ball))
                elif event.text == "d":
                    robot.turnRight()
                if event.text == "w":
                    robot.foreward()
                if event.text == "q":
                    if getBallDist(robot, ball)< 5:
                        robot.grabBall(ball)
                elif event.text == "x":
                    robot.throwBall()
                updateBall(robot, ball)
                #print(robot.front[2])

def draw_score(window, score):
    # create a font object.
    # 1st parameter is the font file
    # which is present in pygame.
    # 2nd parameter is size of the font
    font = pygame.font.Font('freesansbold.ttf', 32)
    
    # create a text surface object,
    # on which text is drawn on it.
    text = font.render(f'Red Team: {score[0]} Blue Team: {score[1]}', True, BLACK, WHITE)
    
    # create a rectangular object for the
    # text surface object
    textRect = text.get_rect()
    textRect.center = (WIDTH // 2, 100)
    # copying the text surface object
    # to the display surface object
    # at the center coordinate.
    WIN.blit(text, textRect)
    
