from OpenGL.GL import *
from OpenGL.GLUT import *
from prettytable import PrettyTable

windowSize = (500, 500)

# (1,1) to (19,19)
division = 15
x_stepsize = 2/division
y_stepsize = 2/division

mytable = PrettyTable(["K", "Pk", "(X_k+1, Y_k+1)"])


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
    p1 = (5, 4)
    p2 = (10, 10)
    Actual(p1, p2)

    x, y = p1[0], p1[1]
    print(f"Initial Point: ({x},{y})")
    Plot(x, y, 'l')
    dx = p2[0]-p1[0]
    dy = p2[1]-p1[1]
    m = (p2[1]-p1[1])/(p2[0]-p1[0])

    x_inc = 1 if dx >= 0 else -1
    y_inc = 1 if dy >= 0 else -1

    stepsize = p2[0]-x
    if (abs(m) >= 1):
        stepsize = p2[1]-y
        x, y = y, x
        x_inc, y_inc = y_inc, x_inc
        dx, dy = dy, dx
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
        plk = pk
        if pk < 0:
            y = y+yl_inc
            if (abs(m) >= 1):
                plx, ply = y, x
                Plot(y, x, 'l')
            else:
                plx, ply = x, y
                Plot(x, y, 'l')
            pk = pk + pkl_inc
        else:
            y = y + ym_inc

            if (abs(m) >= 1):
                plx, ply = y, x
                Plot(y, x, 'l')
            else:
                plx, ply = x, y
                Plot(x, y, 'l')
            pk = pk + pkm_inc
        mytable.add_row(
            [abs(iteration), plk, (plx, ply)])
        iteration = iteration + x_inc


def BLA():

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
    glutCreateWindow("Nirbhay Adhikari (02) BLA")
    glutDisplayFunc(BLA)
    glutMainLoop()


main()
