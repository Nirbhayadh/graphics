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


def Clip(Lp, Wp1, Wp3, delx,dely):
    xwmin, ywmin=Wp1[0], Wp1[1]
    xwmax, ywmax=Wp3[0], Wp3[1]
    x,y = Lp[0], Lp[1]
    P=[-delx, delx, -dely, dely]
    q= [x-xwmin, xwmax- x, y-ywmin, ywmax-y]
    r=[-1,-1,-1,-1]
    for i in range(4):
        if P[i]==0:
            if q[i]<0:
                return (1,0)
            else:
                r[i]=[0]
                continue
        r[i]= round(q[i]/P[i],2)
    inout=[0]
    outin=[1]
    for i in range(0,4):
        if P[i]==0:
            continue
        elif P[i]<0:
            inout.append(r[i])
        else:
            outin.append(r[i])
    u1=max(inout)
    u2=min(outin)
    return u1,u2








def Triangle():
    Wp1=(-5,-5)
    Wp2= (-5,+5)
    Wp3= (5,5)
    Wp4=(5,-5)
    Lp1=(-4,-8)
    Lp2=(-8,-4)
    x1,y1=Lp1        
    Window(Wp1, Wp2, Wp3, Wp4) 
    Line(Lp1,Lp2)
    delx=Lp2[0]-Lp1[0]
    dely=Lp2[1]-Lp1[1]
    u1,u2=Clip(Lp1, Wp1, Wp3, delx,dely)
    if u2<u1:
        print("The entire line lies outside the Window")
        return
    clippedL1=[x1 + u1*delx, y1 + u1*dely]
    clippedL2=[x1+u2*delx, y1 + u2*dely]
    print(f"Given Coordinates: ")
    print(f"(x1,y1) = {Lp1}, (x2,y2) = {Lp2}")
    print(f"Clipped coordinates: ")
    print(f"[x1,y1] = {clippedL1}, [x2,y2] = {clippedL2}")
    Line(clippedL1, clippedL2,"c")



    
    

   
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
    glutCreateWindow("Liang Barsky")
    glutDisplayFunc(Transformations)
    glutMainLoop()


main()
