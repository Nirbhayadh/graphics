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


def Actual(p1, p2, p3):
    glColor3f(0.0, 1.0, 0.0)
    glPointSize(3.0)
    glBegin(GL_LINE_LOOP)
    glVertex2f(p1[0] * x_stepsize, p1[1] * y_stepsize)
    glVertex2f(p2[0] * x_stepsize, p2[1] * y_stepsize)
    glVertex2f(p3[0] * x_stepsize, p3[1] * y_stepsize)


    glEnd()

def Translation(p1, p2, p3, Tr):
    matrix= np.array([[p1[0], p2[0], p3[0]],
                      [p1[1], p2[1], p3[1]],
                      [1,1,1]])
    Tr= np.array([
        [1,0,Tr[0]],
        [0,1,Tr[1]],
        [0,0,1]
    ])
    mul= np.matmul(Tr, matrix)
    p1d=(round(float(mul[0][0]),2),round(float(mul[1][0]),2))
    p2d=(round(float(mul[0][1]),2),round(float(mul[1][1]),2))
    p3d=(round(float(mul[0][2]),2),round(float(mul[1][2]),2))
    print(p1d)
    print(p2d)
    print(p3d)
    Actual(p1d, p2d, p3d) 

def Rotation(p1, p2, p3, theta, Rot):
    theta= (pi/ 180) * theta
    matrix= np.array([[p1[0], p2[0], p3[0]],
                      [p1[1], p2[1], p3[1]],
                      [1,1,1]])
    Rt= np.array([
        [cos(theta),-sin(theta),0],
        [sin(theta),cos(theta),0],
        [0,0,1]
    ])
    Tr=np.array([
        [1,0,-Rot[0]],
        [0,1,-Rot[1]],
        [0,0,1]
    ])
    Trd=np.array([
        [1,0,Rot[0]],
        [0,1,Rot[1]],
        [0,0,1]
    ])
    mul=Trd.dot(Rt).dot(Tr).dot(matrix)
    p1d=(round(float(mul[0][0]),2),round(float(mul[1][0]),2))
    p2d=(round(float(mul[0][1]),2),round(float(mul[1][1]),2))
    p3d=(round(float(mul[0][2]),2),round(float(mul[1][2]),2))
    print(p1d)
    print(p2d)
    print(p3d)
    Actual(p1d, p2d, p3d) 

def Scaling(p1, p2, p3, Scl, Sx, Sy):
    matrix= np.array([[p1[0], p2[0], p3[0]],
                      [p1[1], p2[1], p3[1]],
                      [1,1,1]])
    Sc= np.array([
        [Sx, 0 ,0],
        [0,Sy,0],
        [0,0,1]
    ])
    Tr=np.array([
        [1,0,-Scl[0]],
        [0,1,-Scl[1]],
        [0,0,1]
    ])
    Trd=np.array([
        [1,0,Scl[0]],
        [0,1,Scl[1]],
        [0,0,1]
    ])
    mul=Trd.dot(Sc).dot(Tr).dot(matrix)
    p1d=(round(float(mul[0][0]),2),round(float(mul[1][0]),2))
    p2d=(round(float(mul[0][1]),2),round(float(mul[1][1]),2))
    p3d=(round(float(mul[0][2]),2),round(float(mul[1][2]),2))
    print(p1d)
    print(p2d)
    print(p3d)
    Actual(p1d, p2d, p3d)

def Reflection(p1, p2, p3, m, b):
    theta= atan(m)
    matrix= np.array([[p1[0], p2[0], p3[0]],
                      [p1[1], p2[1], p3[1]],
                      [1,1,1]])

    Rt= np.array([
        [cos(theta),sin(theta),0],
        [-sin(theta),cos(theta),0],
        [0,0,1]
    ])
    Rtd= np.array([
        [cos(theta),-sin(theta),0],
        [sin(theta),cos(theta),0],
        [0,0,1]
    ])

    Ref=np.array([
        [1,0,0],
        [0,-1,0],
        [0,0,1]
        ])
    
    Tr=np.array([
        [1,0,0],
        [0,1,-b],
        [0,0,1]
    ])
    Trd=np.array([
        [1,0,0],
        [0,1,b],
        [0,0,1]
    ])
    mul=Trd.dot(Rtd).dot(Ref).dot(Rt).dot(Tr).dot(matrix)
    p1d=(round(float(mul[0][0]),2),round(float(mul[1][0]),2))
    p2d=(round(float(mul[0][1]),2),round(float(mul[1][1]),2))
    p3d=(round(float(mul[0][2]),2),round(float(mul[1][2]),2))
    print(p1d)
    print(p2d)
    print(p3d)
    Actual(p1d, p2d, p3d)

def Shearing(p1, p2, p3, dir,Sh, ref):
    matrix= np.array([[p1[0], p2[0], p3[0]],
                      [p1[1], p2[1], p3[1]],
                      [1,1,1]])
    if dir=="Y":

        Sh= np.array([
            [1,Sh,-Sh * ref],
            [0,1,0],
            [0,0,1]
        ])
    else:
        Sh= np.array([
            [1,0,0],
            [Sh,1,-Sh * ref],
            [0,0,1]
        ])




    mul=np.matmul(Sh , matrix)
    p1d=(round(float(mul[0][0]),2),round(float(mul[1][0]),2))
    p2d=(round(float(mul[0][1]),2),round(float(mul[1][1]),2))
    p3d=(round(float(mul[0][2]),2),round(float(mul[1][2]),2))
    print(p1d)
    print(p2d)
    print(p3d)
    Actual(p1d, p2d, p3d)


def Triangle():
    p1=(0,0)
    p2= (5,0)
    p3= (0,5)
    print(p1)
    print(p2)
    print(p3)
    print("*****************")
    Actual(p1, p2, p3) 
    ##Translation
    Tr=(3.5,4)
    # Translation(p1, p2, p3, Tr)
    ##Rotation
    Rot=(0,1)
    theta=180
    # Rotation(p1,p2,p3,theta,Rot)
    ##Scaling
    Sx, Sy= 1.5,1.4
    Scl=(0,5)
    # Scaling(p1,p2, p3, Scl, Sx, Sy)
    ##Reflection
    m = 1
    b=1
    # Reflection(p1,p2,p3, m,b)
    ##Shearing
    dir="X"
    Sh=1/2
    ref=-1
    Shearing(p1, p2, p3, dir,Sh, ref)

    
    
    
    



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
    glutCreateWindow("Nirbhay Adhikari (02) Transformations")
    glutDisplayFunc(Transformations)
    glutMainLoop()


main()
