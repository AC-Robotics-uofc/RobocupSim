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
stop = False


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

    deg = round(math.degrees(math.atan(abs(yDiff)/abs(xDiff))))+deg
    deg -= 180
    if(deg < 0):
        deg += 360
    return deg
    #gets angle from positive x axis to hypotenuse 
    
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
        robot.turnRight(abs(robot.front[2]-deg))
    elif robot.front[2]< deg:
        robot.turnLeft(abs(robot.front[2]-deg))


def algorithm(robot, ball, goal):
    ballDist = getBallDist(robot, ball)
    ballAngle = 0
    if ballDist != 0:
        ballDist = getRBD(robot, ball)

    print("ROBOT: x=", robot.front[0], ", y=", robot.front[1])
    print("BALL: x=", ball.xpos, ", y=", ball.ypos)

    print("rbd = ", ballAngle)
    print("robot angle = ", robot.front[2])
    print("robot ball dist = ", ballDist)
        
    global stop 

    if stop == True:
        return
    if robot.hasball == True:
        print("MOVING TO GOAL")
        goalDist = getBallDist(robot, goal)
        goalAngle = getRBD(robot, goal)
        print("goal distance = ", goalDist)
        print("goal deg = ", goalAngle)
        if (abs(robot.front[2] - goalAngle) <= 5 or 170 <= abs(robot.front[2] - goalAngle) <= 190) and goalDist > 100:
            print("GOING TOWARDS GOAL")
            robot.foreward()
            #move towards the goal 
        elif goalDist <= 100:
            print("SHOOTING BALL")
            robot.throwBall()
            stop = True
            #throw the ball then stop moving
        else:
            print("TURNING TOWARD GOAL")
            setDeg(robot, goalAngle)
    elif ballDist < 5:
        print("GRABBING BALL")
        robot.grabBall(ball)
        #if right at the ball, grab it 
    elif abs(robot.front[2] - ballAngle) <= 5 or ballAngle <= 10 or ballDist < 15:
        print("MOVING FOREWARD")
        print("x = ", robot.front[0], ", y = ", robot.front[1])
        robot.foreward()
        #move towards the ball 
    elif ballAngle % 90 == 0 and ballAngle % 180 != 0:
        print("TURNING 1")
        ballAngle -= 180
        if(ballAngle < 0):
            ballAngle += 360
        setDeg(robot, ballAngle)
        #handle %180 case separately because robot gets confused
    else:
        print("TURNING 2")
        setDeg(robot, ballAngle)
        #set degree 
    updateBall(robot, ball)
    
def control(robot, event, ball):
     if event.type == pygame.TEXTINPUT:
                if event.text =="r":
                    robot.up()
                elif event.text == "s":
                    robot.backward()

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
    textRed = font.render(f'Red Team: {score[0]}', True, RED, WHITE)
    textBlue = font.render(f'Blue Team: {score[1]}', True, BLUE, WHITE)

    
    # create a rectangular object for the
    # text surface object
    textRedRect = textRed.get_rect()
    textRedRect.center = (WIDTH // 2 - 150, 100)

    textBlueRect = textBlue.get_rect()
    textBlueRect.center = (WIDTH // 2 + 150, 100)

    # copying the text surface object
    # to the display surface object
    # at the center coordinate.
    WIN.blit(textRed, textRedRect)
    WIN.blit(textBlue, textBlueRect)
    
def resetScore():
    score = [0,0]