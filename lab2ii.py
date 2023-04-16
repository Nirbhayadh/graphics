from OpenGL.GL import *
from OpenGL.GLUT import *
from math import floor

windowSize = (500, 500)
print(windowSize)

# (1,1) to (19,19)
division = 20
x_stepsize = 2/division
y_stepsize = 2/division


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
    glVertex2f(x, y)
    glEnd()


def Points():
    for i in range(1, division):
        for j in range(1, division):
            Plot(i, j, 'p')


def Line():
    p1 = (1, 1)
    p2 = (11, 15)
    # p2 = (11, 1)
    # p1 = (6, 6)
    # p1 = (20, 10)
    # p2 = (30, 18)

    # p1 = (30, 18)
    # p2 = (20, 10)

    # p1 = (20, 10)
    # p2 = (10, 18)

    # p1 = (10, 18)
    # p2 = (20, 10)

    # p1 = (20, 10)
    # p2 = (28, 22)

    # p1 = (28, 22)
    # p2 = (20, 10)

    # p1 = (20, 10)
    # p2 = (12, 22)

    # p1 = (12, 22)
    # p2 = (20, 10)

    x, y = p1[0], p1[1]
    Plot(x, y, 'l')
    dx = p2[0]-p1[0]
    dy = p2[1]-p1[1]
    m = (p2[1]-p1[1])/(p2[0]-p1[0])

    x_inc = 1 if dx >= 0 else -1
    y_inc = 1 if dy >= 0 else -1

    print(x_inc)
    print(y_inc)
    stepsize = p2[0]-x
    if (abs(m) >= 1):
        stepsize = p2[1]-y
        x, y = y, x
        x_inc, y_inc = y_inc, x_inc
        dx, dy = dy, dx
    print(stepsize)
    if dy >= 0:
        dx = dx if dx >= 0 else abs(dx)
        dy = dy if dx >= 0 else abs(dy)
        pkl_inc = 2*dy
        pkm_inc = 2*dy-2*dx
        yl_inc = 0
        ym_inc = y_inc
    else:
        dx = -abs(dx) if dy < 0 else -dx
        dy = -abs(dy) if dy < 0 else -dy
        pkl_inc = 2*dy-2*dx
        pkm_inc = 2*dy
        yl_inc = y_inc
        ym_inc = 0

    iteration = 0
    p0 = 2*dy-dx
    pk = p0
    while (iteration != stepsize):
        x = x + x_inc
        if pk < 0:
            y = y+yl_inc

            # print(y, x)
            if (abs(m) >= 1):
                print(y, x)
                Plot(y, x, 'l')
            else:
                print(x, y)
                Plot(x, y, 'l')
            pk = pk + pkl_inc
        else:
            y = y + ym_inc

            if (abs(m) >= 1):
                print(y, x)
                Plot(y, x, 'l')
            else:
                print(x, y)
                Plot(x, y, 'l')
            pk = pk + pkm_inc
        iteration = iteration + x_inc


def BLA():

    glClear(GL_COLOR_BUFFER_BIT)
    Points()
    Line()

    glFlush()


def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGB)
    glutInitWindowSize(windowSize[0], windowSize[1])
    glutInitWindowPosition(500, 50)
    glutCreateWindow("Nirbhay Adhikari (02)")
    glutDisplayFunc(BLA)
    glutMainLoop()


main()
