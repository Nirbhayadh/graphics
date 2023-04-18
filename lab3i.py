from OpenGL.GL import *
from OpenGL.GLUT import *
import math

windowSize = (500, 500)
division = 15
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


def Actual(cx, cy, radius):
    glColor3f(0.0, 1.0, 0.0)
    glPointSize(3.0)
    triangles = 100
    glBegin(GL_LINE_LOOP)
    for i in range(0, 100):
        x = cx+radius*math.cos(i * 2*math.pi/triangles)
        y = cy+radius*math.sin(i * 2*math.pi/triangles)
        x = 0+x*x_stepsize
        y = 0+y*y_stepsize
        glVertex2f(x, y)

    glEnd()


def PlotSymmetry(x, y):
    Plot(x, y, 'l')
    Plot(y, x, 'l')
    Plot(x, -y, 'l')
    Plot(y, -x, 'l')
    Plot(-x, -y, 'l')
    Plot(-y, -x, 'l')
    Plot(-x, y, 'l')
    Plot(-y, x, 'l')


def Circle():
    cx, cy = 0, 0
    ox, oy = 0, 0
    radius = 4
    Actual(cx, cy, radius)
    x, y = ox, radius
    PlotSymmetry(x+cx, y+cy)
    p0 = 5/4-radius
    pk = p0
    while (x < y):
        x = x+1
        if (pk < 0):
            pk = pk+2*x+1
        else:
            y = y-1
            pk = pk+2*x+1-2*y
        print(x, y)
        PlotSymmetry(x, y)


def MIDCIRCLE():
    glClear(GL_COLOR_BUFFER_BIT)
    Points()
    Circle()
    glFlush()


def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGB)
    glutInitWindowSize(windowSize[0], windowSize[1])
    glutInitWindowPosition(300, 100)
    glutCreateWindow("Nirbhay Adhikari (02) DDA")
    glutDisplayFunc(MIDCIRCLE)
    glutMainLoop()


main()
