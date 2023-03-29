from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math
import numpy

def bluePart():
    vertices1 = (
    (-0.02,0.38),
    (-0.02,0.85),
    (0.70,0.38),
    )
    vertices2 = (
    (-0.02, -0.02),
    (-0.02, 0.6),
    (0.70,-0.02),
    )
    ##Upper Half
    glColor3f(0.0,0.0,1.0)
    glBegin(GL_TRIANGLES)
    for vertex in vertices1:
        x = vertex[0]
        y = vertex[1]
        glVertex2f(x,y)
    glEnd()
    #Lower Half
    glColor3f(0.0,0.0,1.0)
    glBegin(GL_TRIANGLES)
    for vertex in vertices2:
        x = vertex[0]
        y = vertex[1]
        glVertex2f(x,y)
    glEnd()

def redPart():
    vertices1 = (
    (0.0,0.4),
    (0,0.8),
    (0.65,0.4),
    )
    vertices2 = (
    (0.0, 0.0),
    (0.0, 0.55),
    (0.65,0.0),
    )
    ##Upper Half
    glColor3f(1.0,0.0,0.0)
    glBegin(GL_TRIANGLES)
    for vertex in vertices1:
        x = vertex[0]
        y = vertex[1]
        glVertex2f(x,y)
    glEnd()
    ##Upper Half
    glColor3f(1.0,0.0,0.0)
    glBegin(GL_TRIANGLES)
    for vertex in vertices2:
        x = vertex[0]
        y = vertex[1]
        glVertex2f(x,y)
    glEnd()

def lowerCircle():
    stepsize=50
    radius=0.09
    angle=2* math.pi  / stepsize
    cx,cy=0.18,0.16
    xi,yi=radius,cy
    for i in range(0,stepsize+1):
        glColor3f(1.0,1.0,1.0)
        glBegin(GL_TRIANGLES)
        glVertex2f(cx,cy)
        glVertex2f(xi,yi)
        nxi=cx+ radius * math.cos(angle*(i+1))
        nyi=cy +radius * math.sin(angle*(i+1))
        glVertex2f(nxi,nyi)
        xi=nxi
        yi=nyi
        glEnd()


def upperLowerCircle():
    stepsize=50
    radius=0.09
    angle=2* math.pi  / stepsize
    cx,cy=0.18,0.55
    xi,yi=radius,cy
    for i in range(0,stepsize+1):        
        nxi=cx+ radius * math.cos(-angle*(i))
        nyi=cy +radius * math.sin(-angle*(i))
        if i in range(int(stepsize/2)+2,stepsize):
            xi=nxi
            yi=nyi
            continue
        glColor3f(1.0,1.0,1.0)
        glBegin(GL_TRIANGLES)
        glVertex2f(cx,cy)
        glVertex2f(xi,yi)        
        glVertex2f(nxi,nyi)     
        xi=nxi
        yi=nyi
        glEnd()


def upperUpperCircle():
    stepsize=8
    radius=0.045
    angle=2* math.pi  / stepsize
    cx,cy=0.18, 0.565
    xi,yi=radius,cy
    for i in range(0,int(stepsize)+1):
        glColor3f(1.0,1.0,1.0)
        glBegin(GL_TRIANGLES)
        glVertex2f(cx,cy)
        glVertex2f(xi,yi)
        nxi=cx+ radius * math.cos(angle*(i))
        nyi=cy +radius * math.sin(angle*(i))
        glVertex2f(nxi,nyi)
        xi=nxi
        yi=nyi
        glEnd()


def flag():
    
    glClear(GL_COLOR_BUFFER_BIT)
    bluePart()
    redPart()
    lowerCircle()
    upperLowerCircle()
    upperUpperCircle()    
    glFlush()

def clearScreen():
    glClearColor(0.0,0.0,0.0,1.0)
    gluOrtho2D(-0.5,1.0,-0.5,1.0)

def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGB)
    glutInitWindowSize(320,320)
    glutInitWindowPosition(100, 100)
    glutCreateWindow("Nirbhay Adhikari (02)")
    glutDisplayFunc(flag)
    clearScreen()

    size = numpy.ndarray.tolist(glGetIntegerv(GL_VIEWPORT))
    size = size[2],size[3]
    print(f'Display Window (Width, Height) :-  {size}' )


    glutMainLoop()   

main()


