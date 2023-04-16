from OpenGL.GL import *
from OpenGL.GLUT import *
from math import ceil

windowSize = (500, 500)
division = 20
x_stepsize = 2/division
y_stepsize = 2/division
print(x_stepsize)
# (1,1) to (19,19)


def Plot(x, y, g):
    if g == 'p':

        glColor3f(1.0, 1.0, 1.0)
        glPointSize(3.0)
    else:
        glColor3f(1.0, 0.0, 0.0)
        glPointSize(8.0)

    glBegin(GL_POINTS)
    x = -1+x*x_stepsize
    # y = -1+y*y_stepsize
    y = round(-1+y*y_stepsize, 1)
    # x = ceil(-1+x*x_stepsize)
    # y = ceil(-1+y*y_stepsize)
    glVertex2f(x, y)
    glEnd()


def Points():
    for i in range(1, division):
        for j in range(1, division):
            Plot(i, j, 'p')


def Line():

    p1 = (1, 1)
    p2 = (11, 10)
    dx = p2[0]-p1[0]
    dy = p2[1]-p1[1]
    m = (p2[1]-p1[1])/(p2[0]-p1[0])
    if (abs(dx) > abs(dy)):
        stepsize = abs(dx)
    else:
        stepsize = abs(dy)
    x_inc = dx/stepsize
    y_inc = dy/stepsize
    x = p1[0]
    y = p1[1]
    Plot(x, y, 'l')

    iteration = 0
    while (iteration != stepsize):
        x = x + x_inc
        y = y + y_inc
        Plot(x, y, 'l')
        iteration = iteration+1


def DDA():

    glClear(GL_COLOR_BUFFER_BIT)
    Points()
    Line()

    glFlush()


def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGB)
    glutInitWindowSize(windowSize[0], windowSize[1])
    glutInitWindowPosition(100, 100)
    glutCreateWindow("Nirbhay Adhikari (02)")
    glutDisplayFunc(DDA)
    glutMainLoop()


main()
