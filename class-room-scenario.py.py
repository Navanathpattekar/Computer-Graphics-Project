import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

pygame.init()

width, height = 800, 700
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Classroom Scene')


# Define colors
WHITE = (1.0, 1.0, 1.0)
BLACK = (0.0, 0.0, 0.0)
BROWN = (0.54, 0.27, 0.07)
LIGHT_BROWN = (0.87, 0.72, 0.53)
BLUE = (0.0, 0.0, 1.0)
GRAY = (0.5, 0.5, 0.5)
DARK_GRAY = (0.66, 0.66, 0.66)
GREEN = (0.13, 0.55, 0.13)
XYZ= (128,128,0)

#  Function to draw the classroom
def draw_classroom():
    glBegin(GL_QUADS)
   
    # Floor
    glColor3fv(DARK_GRAY)
    glVertex3f(-14, -3, -10)
    glVertex3f(15, -3, -10)
    glVertex3f(17, -6, 10)
    glVertex3f(-16, -6, 10)

    pygame.draw.rect(screen, DARK_GRAY, [0, height - 200, width, 200])
    
    # Back wall
    glColor3fv(LIGHT_BROWN)
    glVertex3f(-15, -3, -10)
    glVertex3f(15, -3, -10)
    glVertex3f(15, 14, -10)
    glVertex3f(-15, 14, -10)
    
    # Left wall
    glVertex3f(-12, -3, -10)
    glVertex3f(-13, -8, 10)
    glVertex3f(-12, 12, 10)
    glVertex3f(-12, 12, -10)
    
    # Right wall
    glVertex3f(15, -3, -10)
    glVertex3f(17, -6, 10)
    glVertex3f(17, 10, 10)
    glVertex3f(15, 14, -10)
    
    # Ceiling
    glColor3fv(WHITE)
    glVertex3f(-15, 13, -10)
    glVertex3f(15, 13, -10)
    glVertex3f(17, 10, 10)
    glVertex3f(-13, 10, 10)
    glEnd()

    # Blackboard
    glBegin(GL_QUADS)
    glColor3fv(BLACK)
    glVertex3f(-8, 4, -9.9)
    glVertex3f(9, 4, -9.9)
    glVertex3f(9, 9, -9.9)
    glVertex3f(-8, 9, -9.9)
    glEnd()

#  desk 
def square(x,y):

    bench_leg(x-0.,y-3.2)
    bench_leg(x+0.9,y-4.3)
    bench_leg(x+4.6,y-4.3)
    bench_leg(x+3.7,y-4.3)
    glColor3fv(BROWN)
    glBegin(GL_POLYGON)
    glVertex3f(x,y,0)
    glVertex3f(x+4,y,0)
    glVertex3f(x+5,y-1,0)
    glVertex3f(x+1,y-1,0)
    glVertex3f(x+1,y-1.3,0)#
    glVertex3f(x+5,y-1.3,0)#
    glVertex3f(x+5,y-1,0)
    glVertex3f(x,y,0)
    glVertex3f(x,y-0.3,0)#
    glVertex3f(x+1,y-1.3,0)
    glEnd()
    

def bench_leg(x,y):
    glColor3fv(GRAY)    
    glBegin(GL_QUADS)
    glVertex3f(x,y,0)
    glVertex3f(x+0.4,y+0,0)
    glVertex3f(x+0.4,y+3,0)
    glVertex3f(x,y+3,0)
    glEnd()   


# table
def table(x,y):

    table_leg(x-0.,y-0.1)
    table_leg(x+0.9,y-1.3)
    table_leg(x+4.6,y-1.3)
    table_leg(x+3.7,y-1.3)
    glColor3fv(XYZ)
    glBegin(GL_POLYGON)
    glVertex3f(x,y-2,0)
    glVertex3f(x+4,y-2,0)
    glVertex3f(x+5,y-3,0)
    glVertex3f(x+1,y-3,0)
    glVertex3f(x+1,y-3.3,0)#
    glVertex3f(x+5,y-3.3,0)#
    glVertex3f(x+5,y-3,0)
    glVertex3f(x,y-2,0)
    glVertex3f(x,y-2.3,0)#
    glVertex3f(x+1,y-2.3,0)
    glEnd()
    

def table_leg(x,y):
    glColor3fv(BLUE)    
    glBegin(GL_QUADS)
    glVertex3f(x,y-2,0)
    glVertex3f(x+0.4,y-2,0)
    glVertex3f(x+0.4,y-4,0)
    glVertex3f(x,y-4,0)
    glEnd()   
    

def f_ground():
    glColor3fv(GREEN)
    glBegin(GL_QUADS)
    glVertex3f(-2,-2,5)
    glVertex3f(-2,-1,5)
    glVertex3f(9,-1,5)
    glVertex3f(9,-2,5)
    glEnd()

    glBegin(GL_QUADS)
    glColor3fv(WHITE)
    glVertex3f(-1.2,0.2,5)
    glVertex3f(-2,-1,5)
    glVertex3f(9,-1,5)
    glVertex3f(9.2,0.2,5)
    glEnd()

    glBegin(GL_QUADS)
    glColor3fv(WHITE)
    glVertex3f(9.2,-0.2,5)
    glVertex3f(9.2,0.2,5)
    glVertex3f(9,-1,5)
    glVertex3f(9,-2,5)
    glEnd()


# bureo
def buero():
    glColor3fv(GREEN)
    glBegin(GL_QUADS)
    glVertex3f(12,3,3)
    glVertex3f(9.9,2.9,3)
    glVertex3f(9.9,-1,3)
    glVertex3f(12,-3,3)
    glEnd()
    
    glBegin(GL_QUADS)
    glColor3fv(BLACK)
    glVertex3f(12,3,3)
    glVertex3f(9.9,2.9,3)
    glVertex3f(11,3.6,3)
    glVertex3f(13,3.6,3)
    glEnd()

    glBegin(GL_QUADS)
    glColor3fv(GREEN)
    glVertex3f(12,3,3)
    glVertex3f(13,3.6,3)
    glVertex3f(13,-2,3)
    glVertex3f(12,-3,3)
    glEnd()

    glBegin(GL_QUADS)
    glColor3fv(BLACK)
    glVertex3f(10.3,2.6,3)
    glVertex3f(11.5,2.6,3)
    glVertex3f(11.5,1.4,3)
    glVertex3f(10.3,1.4,3)
    glEnd()

    glBegin(GL_QUADS)
    glColor3fv(BLACK)
    glVertex3f(10.3,1,3)
    glVertex3f(11.5,1,3)
    glVertex3f(11.5,0,3)
    glVertex3f(10.3,0,3)
    glEnd()

    glBegin(GL_QUADS)
    glColor3fv(BLACK)
    glVertex3f(10.3,-0.2,3)
    glVertex3f(11.5,-0.2,3)
    glVertex3f(11.5,-1.1,3)
    glVertex3f(10.3,-1.1,3)
    glEnd()


# projector
def projector():
    
    glBegin(GL_QUADS)
    glColor3fv(GRAY)
    glVertex3f(-0.8,15,-6)
    glVertex3f(0.8,15,-6)
    glVertex3f(0.8,10,-6)
    glVertex3f(-0.8,10,-6)
    glEnd()

    glBegin(GL_QUADS)
    glColor3fv(BLUE)
    glVertex3f(3,10,-6)
    glVertex3f(3,12,-6)
    glVertex3f(-3,12,-6)
    glVertex3f(-3,10,-6)
    glEnd()

def draw_chair():
    
    # Seat
    glColor3fv(BROWN)  
    glPushMatrix()
    glTranslatef(-2, 1, 0)
    draw_colored_cube(2, 0.2, 2)
    glPopMatrix()
    
    # Backrest (front view)
    glPushMatrix()
    glTranslatef(-2, 2.2, 0.9)
    glColor3fv(BROWN)  # Brown color
    draw_colored_cube(2, 2, 0.2)
    glPopMatrix()

    # Legs
    glPushMatrix()
    glTranslatef(-2.9, 0.5, -0.9)
    draw_colored_cube(0.2, 1, 0.2)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(-2, 0.5, -0.9)
    draw_colored_cube(0.2, 1, 0.2)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(-2.9, 0.5, 0.9)
    draw_colored_cube(0.2, 1, 0.2)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(-0.4, 0.5, 0.9)
    draw_colored_cube(0.2, 1, 0.2)
    glPopMatrix()

def draw_colored_cube(width, height, depth):
    vertices = [
        (width / 2, -height / 2, -depth / 2),
        (width / 2, height / 2, -depth / 2),
        (-width / 2, height / 2, -depth / 2),
        (-width / 2, -height / 2, -depth / 2),
        (width / 2, -height / 2, depth / 2),
        (width / 2, height / 2, depth / 2),
        (-width / 2, -height / 2, depth / 2),
        (-width / 2, height / 2, depth / 2)
    ]

    edges = (
        (0, 1), (1, 2), (2, 3), (3, 0),
        (4, 5), (5, 6), (6, 7), (7, 4),
        (0, 4), (1, 5), (2, 6), (3, 7)
    )

    surfaces = (
        (0, 1, 2, 3),
        (3, 2, 7, 6),
        (6, 7, 5, 4),
        (4, 5, 1, 0),
        (1, 5, 7, 2),
        (4, 0, 3, 6)
    )

    glBegin(GL_QUADS)
    for surface in surfaces:
        for vertex in surface:
            glVertex3fv(vertices[vertex])
    glEnd()

def teature():
    glColor3fv(GREEN)
    glBegin(GL_QUADS)
    glVertex3f(1,4,0)
    glVertex3f(2,4,0)
    glVertex3f(2,2,0)
    glVertex3f(1,2,0)
    glEnd()
    
    glColor3fv(BLACK)
    glBegin(GL_QUADS)
    glVertex3f(1,2,0)
    glVertex3f(1.2,2,0)
    glVertex3f(1.2,0,0)
    glVertex3f(1,0,0)
    glEnd()

    glColor3fv(BLACK)
    glBegin(GL_QUADS)
    glVertex3f(2,2,0)
    glVertex3f(1.8,2,0)
    glVertex3f(1.8,0,0)
    glVertex3f(2,0,0)
    glEnd()

    glColor3fv(GREEN)
    glBegin(GL_QUADS)
    glVertex3f(-1,3.8,0)
    glVertex3f(1,4,0)
    glVertex3f(1,3.6,0)
    glVertex3f(-1,3.6,0)
    glEnd()

    glColor3fv(GREEN)
    glBegin(GL_QUADS)
    glVertex3f(2,4,0)
    glVertex3f(4,3.8,0)
    glVertex3f(4,3.6,0)
    glVertex3f(2,3.6,0)
    glEnd()

    glColor3fv(WHITE)
    glBegin(GL_POLYGON)
    glVertex3f(0,4,0)
    glVertex3f(-0.1,4,0)
    glVertex3f(-0.2,4.6,0)
    glVertex3f(-0.3,4.7,0)
    glVertex3f(-0.2,4,0)
    glVertex3f(-0.1,4.1,0)
    glVertex3f(0,4,0)
    glVertex3f(0.1,4.1,0)
    glVertex3f(0.2,4,0)
    glVertex3f(0.3,4.7,0)
    glVertex3f(0.2,4.6,0)
    glVertex3f(0.1,4.5,0)
    glVertex3f(0,4,0)
    glEnd()
 
 
 

def main():
    pygame.init()
    display=(800,600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
   
    gluPerspective(80,(display[0]/display[1]),0.1,50.0)
    
    glTranslate(-2,0,-5)

    # glRotatef(25, 2, 1, 0)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    glTranslatef(-0.5,0,0)
                if event.key == pygame.K_RIGHT:
                    glTranslatef(0.5,0,0)
                if event.key == pygame.K_UP:
                    glTranslatef(0,0.5,0)
                if event.key == pygame.K_DOWN:
                    glTranslatef(0,-0.5,0)
                if event.key == pygame.K_x:
                    glRotatef(15,1,1,0)
                

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glPushMatrix()
        glScalef(0.3,0.3,0.3)
        draw_classroom()
        f_ground()

        teature()

        projector()
        buero()
        
        # benches
        # 1st column
        square(-5,-1.8)
        table(-5,-2)
        square(-6.2,-3.4)
        table(-6.2,-3.8)
        square(-8,-7)
        table(-8,-8)
        
        # 2nd column
        square(2.4,-1.2)
        table(2.4,-2)
        square(2,-3.2)
        table(2,-5)
        square(1.6,-6.2)
        table(1.6,-8)
        
        # 3rd column
        square(10,-1.2)
        table(10,-2)
        square(9.8,-3.2)
        table(9.8,-5)
        square(10,-6.2)
        table(10,-8)
        

        draw_chair()
        square(-4.6,2.8)
        
        glPopMatrix()
        
        pygame.display.flip()
        pygame.time.wait(10)
main()
 