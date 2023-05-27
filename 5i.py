from OpenGL.GL import *
from OpenGL.GLUT import *
from math import sin, cos, pi, atan
import numpy as np

windowSize = (500, 500)
division = 22
x_stepsize = 2/division
y_stepsize = 2/division

def Plot(x, y, g):
    if g == 'p':

        glColor3f(1.0, 1.0, 1.0)
        glPointSize(3.0)
    else:
        glColor3f(1.0, 0.0, 0.0)
        glPointSize(5.0)

    glBegin(GL_POINTS)
    x = 0+x*x_stepsize
    y = 0+y*y_stepsize
    glVertex2f(x, y)
    glEnd()


def Points():
    for i in range(int(-division/2)+1, int(division/2)):
        for j in range(int(-division/2)+1, int(division/2)):
            Plot(i, j, 'p')


def Window(Wp1, Wp2, Wp3, Wp4):
    glColor3f(0.0, 1.0, 0.0)
    glPointSize(3.0)
    glBegin(GL_LINE_LOOP)
    glVertex2f(Wp1[0] * x_stepsize, Wp1[1] * y_stepsize)
    glVertex2f(Wp2[0] * x_stepsize, Wp2[1] * y_stepsize)
    glVertex2f(Wp3[0] * x_stepsize, Wp3[1] * y_stepsize)
    glVertex2f(Wp4[0] * x_stepsize, Wp4[1] * y_stepsize)


    glEnd()

def Line(Lp1, Lp2, c=None):    
    glColor3f(1.0, .0, .0)  
    
    if c=="c":
        glColor3f(0.0, 1.0, 1.0)
              
    glPointSize(3.0)
    glBegin(GL_LINES)
    glVertex2f(Lp1[0] * x_stepsize, Lp1[1] * y_stepsize)
    glVertex2f(Lp2[0] * x_stepsize, Lp2[1] * y_stepsize)
    glEnd()

def Region(Lp, Wp1, Wp3):
    xmin, ymin=Wp1[0], Wp1[1]
    xmax, ymax=Wp3[0], Wp3[1]
    x,y = Lp[0], Lp[1]
    code=[0,0,0,0]
    if x<xmin:
        code[3]=1
    if x>xmax:
        code[2]=1
    if y<ymin:
        code[1]=1
    if y>ymax:
        code[0]=1

    return code


def CodeAnd(code1,code2):
    sp=[0,0,0,0]
    for i in range(4):

        sp[i]=code1[i] & code2[i]
    return sp

def clippedPoint(Code,Wp1,Wp3,x1,y1,m):
    
    if Code[3]==1:
        x=Wp1[0]                    
        y=y1 + m * (x - x1)
    elif Code[2]==1:
        x=Wp3[0]                    
        y=y1 + m * (x - x1)
    elif Code[1]==1:
        y=Wp1[1]          
        try:

            x=(y - y1 )/ m + x1
        except:
            x=x1
    elif Code[0]==1:
        y=Wp3[1]   
        try:                 
            x=(y - y1 )/ m + x1
        except:
            x=x1
    Code=Region((x,y),Wp1,Wp3)
    point=(x,y)
    return Code, point


def Triangle():
    Wp1=(-5,-5)
    Wp2= (-5,+5)
    Wp3= (5,5)
    Wp4=(5,-5)
    Lp1=(-2,-10)
    Lp2=(-8,2)

    try:
        m=(Lp2[1]- Lp1[1]) / (Lp2[0]- Lp1[0])
    except:
        m=None

    Window(Wp1, Wp2, Wp3, Wp4) 
    Line(Lp1,Lp2)
    code1=Region(Lp1,Wp1,Wp3)
    code2=Region(Lp2,Wp1,Wp3)

    if code1 == code2 == [0,0,0,0]:
        print("The Line lies entirely inside the Window")
        Line(Lp1,Lp2,"c")
        return

    x1,y1=Lp1[0], Lp1[1]
    u=Lp1
    v=Lp2
    while CodeAnd(code1,code2) == [0,0,0,0] and (code1!=[0,0,0,0] or code2!=[0,0,0,0]):    
        if code1!=[0,0,0,0]:
           code1,u= clippedPoint(code1,Wp1,Wp3,x1,y1,m)
      
        
        elif code2!=[0,0,0,0]:
            code2,v= clippedPoint(code2,Wp1,Wp3,x1,y1,m)
      

    if code1==code2==[0,0,0,0]:
        Line(u,v,"c")
    else:
        print("The Entire Line lies Outside the Window")
        return





   
def Transformations():
    glClear(GL_COLOR_BUFFER_BIT)
    Points()
    Triangle()
    glFlush()


def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGB)
    glutInitWindowSize(windowSize[0], windowSize[1])
    glutInitWindowPosition(600, 100)
    glutCreateWindow("Cohen Sutherland")
    glutDisplayFunc(Transformations)
    glutMainLoop()


main()
