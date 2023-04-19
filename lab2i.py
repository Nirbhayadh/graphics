from OpenGL.GL import *
from OpenGL.GLUT import *
from prettytable import PrettyTable

windowSize = (500, 500)
division = 15
x_stepsize = 2/division
y_stepsize = 2/division

mytable = PrettyTable(["Step", "Calculated (x,y)", "Plot (x,y)"])


def Plot(x, y, g):
    if g == 'p':

        glColor3f(1.0, 1.0, 1.0)
        glPointSize(3.0)
    else:
        glColor3f(1.0, 0.0, 0.0)
        glPointSize(5.0)

    glBegin(GL_POINTS)
    x = -1+x*x_stepsize
    y = -1+y*y_stepsize
    glVertex2f(x, y)
    glEnd()


def Points():
    for i in range(1, division):
        for j in range(1, division):
            Plot(i, j, 'p')


def Actual(p1, p2):
    glColor3f(0.0, 1.0, 0.0)
    glPointSize(3.0)
    glBegin(GL_LINES)
    glVertex2f(-1+p1[0]*x_stepsize, -1+p1[1]*y_stepsize)
    glVertex2f(-1+p2[0]*x_stepsize, -1+p2[1]*y_stepsize)
    glEnd()


def Line():
    p1 = (10, 10)
    p2 = (5, 4)
    Actual(p1, p2)
    dx = p2[0]-p1[0]
    dy = p2[1]-p1[1]
    if (abs(dx) > abs(dy)):
        stepsize = abs(dx)
    else:
        stepsize = abs(dy)
    x_inc = dx/stepsize
    y_inc = dy/stepsize
    x = p1[0]
    y = p1[1]
    print(f"Initial Point: ({x},{y})")
    Plot(x, y, 'l')
    iteration = 0
    while (iteration != stepsize):
        x = x + x_inc
        y = y + y_inc

        mytable.add_row(
            [iteration+1, (round(x, 3), round(y, 3)), (round(x), round(y))])
        Plot(round(x), round(y), 'l')
        iteration = iteration+1


def DDA():

    glClear(GL_COLOR_BUFFER_BIT)
    Points()
    Line()
    print(mytable)
    glFlush()


def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGB)
    glutInitWindowSize(windowSize[0], windowSize[1])
    glutInitWindowPosition(600, 100)
    glutCreateWindow("Nirbhay Adhikari (02) DDA")
    glutDisplayFunc(DDA)
    glutMainLoop()


main()
