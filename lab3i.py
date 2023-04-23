from OpenGL.GL import *
from OpenGL.GLUT import *
import math
from prettytable import PrettyTable

windowSize = (500, 500)
division = 15
x_stepsize = 2/division
y_stepsize = 2/division

mytable = PrettyTable(["K", "Pk", "(X_k+1, Y_k+1)",
                      "2 * X_k+1", "2 * Y_k+1", "(X_k+1 + Cx, Y_k+1 + Cy)"])


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
    for i in range(0, triangles):
        x = cx+radius*math.cos(i * 2*math.pi/triangles)
        y = cy+radius*math.sin(i * 2*math.pi/triangles)
        x = 0+x*x_stepsize
        y = 0+y*y_stepsize
        glVertex2f(x, y)

    glEnd()


def PlotSymmetry(x, y, cx, cy):
    Plot(x+cx, y+cy, 'l')
    Plot(y+cx, x+cy, 'l')
    Plot(x+cx, -y+cy, 'l')
    Plot(y+cx, -x+cy, 'l')
    Plot(-x+cx, -y+cy, 'l')
    Plot(-y+cx, -x+cy, 'l')
    Plot(-x+cx, y+cy, 'l')
    Plot(-y+cx, x+cy, 'l')


def Circle():
    cx, cy = 2, 2
    ox, oy = 0, 0
    radius = 4
    Actual(cx, cy, radius)
    x, y = ox, radius
    print(f"Starting Point: ({x+cx},{y+cy})")
    PlotSymmetry(x, y, cx, cy)
    p0 = 1-radius
    pk = p0
    while (x < y):
        plk = pk
        x = x+1
        if (pk < 0):
            pk = pk+2*x+1
        else:
            y = y-1
            pk = pk+2*x+1-2*y
        mytable.add_row(
            [x-1, plk, (x, y), 2 * x, 2 * y, (x+cx, y+cy)])
        PlotSymmetry(x, y, cx, cy)


def MIDCIRCLE():
    glClear(GL_COLOR_BUFFER_BIT)
    Points()
    Circle()
    print(mytable)
    glFlush()


def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGB)
    glutInitWindowSize(windowSize[0], windowSize[1])
    glutInitWindowPosition(600, 100)
    glutCreateWindow("Nirbhay Adhikari (02) MIDCIRCLE")
    glutDisplayFunc(MIDCIRCLE)
    glutMainLoop()


main()
