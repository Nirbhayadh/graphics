from OpenGL.GL import *
from OpenGL.GLUT import *
from math import sqrt, pow
import math
from prettytable import PrettyTable


windowSize = (500, 500)
division = 30
x_stepsize = 2/division
y_stepsize = 2/division

mytable1 = PrettyTable(["K", "P1k", "(X_k+1, Y_k+1)", "2*Ry.sq*X_k+1", "2*Rx.sq*Y_k+1",
                       "(X_k+1 + Cx, Y_k+1 + Cy)"])
mytable2 = PrettyTable(["K", "P2k", "(X_k+1, Y_k+1)",
                       "(X_k+1 + Cx, Y_k+1 + Cy)"])


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


def Actual(cx, cy, rx, ry):

    glColor3f(0.0, 1.0, 0.0)
    glPointSize(3.0)
    glBegin(GL_LINE_LOOP)
    triangles = 400
    for i in range(0, triangles):
        x = cx+rx*math.cos(i * 2*math.pi/triangles)
        y = cy+ry*math.sin(i * 2*math.pi/triangles)
        x = 0+x*x_stepsize
        y = 0+y*y_stepsize
        glVertex2f(x, y)
    glEnd()


def PlotSymmetry(x, y, cx, cy):
    Plot(x+cx, y+cy, 'l')
    Plot(x+cx, -y+cy, 'l')
    Plot(-x+cx, y+cy, 'l')
    Plot(-x+cx, -y+cy, 'l')


def Ellipse():
    cx, cy = 0, 0
    ox, oy = 0, 0
    rx, ry = 8, 6
    Actual(cx, cy, rx, ry)
    x, y = ox, ry
    print(f"Starting Point (First Part): ({x+cx},{y+cy})")
    PlotSymmetry(x, y, cx, cy)
    p10 = pow(ry, 2)-pow(rx, 2)*ry + pow(rx, 2)/4
    p1k = p10
    while (2*pow(ry, 2)*x < 2*pow(rx, 2)*y):
        pl1k = p1k
        x = x+1
        if (p1k < 0):
            p1k = p1k+2*pow(ry, 2)*x + pow(ry, 2)
        else:
            y = y-1
            p1k = p1k+2*pow(ry, 2)*x + pow(ry, 2) - 2*pow(rx, 2)*y
        mytable1.add_row([x-1, pl1k, (x, y), 2*pow(ry, 2)
                          * x, 2*pow(rx, 2)*y, (x+cx, y+cy)])
        PlotSymmetry(x, y, cx, cy)
    print(mytable1)
    p20 = pow(ry, 2)*pow(x+0.5, 2) + \
        pow(rx, 2)*pow(y-1, 2) - pow(rx, 2)*pow(ry, 2)
    p2k = p20
    print(f"Starting Point (Second Part): ({x+cx},{y+cy})")
    count = 0
    while (y > 0):
        pl2k = p2k
        y = y-1
        if (p2k <= 0):
            x = x+1
            p2k = p2k+2*pow(ry, 2)*x + pow(rx, 2) - 2*pow(rx, 2)*y
        else:
            p2k = p2k + pow(rx, 2) - 2*pow(rx, 2)*y
        mytable2.add_row([count, pl2k, (x, y),  (x+cx, y+cy)])
        PlotSymmetry(x, y, cx, cy)
        count += 1
    print(mytable2)


def MIDELLIPSE():
    glClear(GL_COLOR_BUFFER_BIT)
    Points()
    Ellipse()

    glFlush()


def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGB)
    glutInitWindowSize(windowSize[0], windowSize[1])
    glutInitWindowPosition(300, 100)
    glutCreateWindow("Nirbhay Adhikari (02) MIDELLIPSE")
    glutDisplayFunc(MIDELLIPSE)
    glutMainLoop()


main()
