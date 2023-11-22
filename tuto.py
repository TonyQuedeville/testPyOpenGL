import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

def loadTexture():
    textureSurface = pygame.image.load('img/vintage-paper.jpg')
    textureData = pygame.image.tostring(textureSurface, "RGBA", 1)
    width = textureSurface.get_width()
    height = textureSurface.get_height()

    glEnable(GL_TEXTURE_2D)
    texid = glGenTextures(1)

    glBindTexture(GL_TEXTURE_2D, texid)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, width, height,
                0, GL_RGBA, GL_UNSIGNED_BYTE, textureData)

    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)

    return texid

def cube(position=(0,0,0), size=1, lines=False):
    x= position[0]
    y= position[1]
    z= position[2]
    
    edges = (
    (0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,7),
    (6,3),
    (6,4),
    (6,7),
    (5,1),
    (5,4),
    (5,7)
    )
    
    verticies = (
        (x-size, y-size, z+size), # 0
        (x+size, y-size, z+size), # 1
        (x+size, y+size, z+size), # 2
        (x-size, y+size, z+size), # 3
        (x-size, y-size, z-size), # 4
        (x-size, y+size, z-size), # 5
        (x+size, y+size, z-size), # 6
        (x+size, y-size, y-size)  # 7  
    )
    
    if lines:
        glBegin(GL_LINES)
        for edge in edges:
            glColor3fv((1, 1, 1))
            for vertex in edge:
                glVertex3fv(verticies[vertex])
        glEnd()
    else:
        glBegin(GL_QUADS)
        
        # Face Avant
        glTexCoord2f(0.0, 0.0)
        glVertex3fv(verticies[0])
        glTexCoord2f(1.0, 0.0)
        glVertex3fv(verticies[1])
        glTexCoord2f(1.0, 1.0)
        glVertex3fv(verticies[2])
        glTexCoord2f(0.0, 1.0)
        glVertex3fv(verticies[3])
        
        # # Face Arrière
        glTexCoord2f(1.0, 0.0)
        glVertex3fv(verticies[4])
        glTexCoord2f(1.0, 1.0)
        glVertex3fv(verticies[5])
        glTexCoord2f(0.0, 1.0)
        glVertex3fv(verticies[6])
        glTexCoord2f(0.0, 0.0)
        glVertex3fv(verticies[7])
        
        # Face Dessus
        glTexCoord2f(0.0, 1.0)      
        glVertex3fv(verticies[5])
        glTexCoord2f(0.0, 0.0)
        glVertex3fv(verticies[3])       
        glTexCoord2f(1.0, 0.0)
        glVertex3fv(verticies[2])        
        glTexCoord2f(1.0, 1.0)
        glVertex3fv(verticies[6])
        
        # Face Dessous
        glTexCoord2f(1.0, 1.0)
        glVertex3fv(verticies[4])
        glTexCoord2f(0.0, 1.0)
        glVertex3fv(verticies[7])
        glTexCoord2f(0.0, 0.0)
        glVertex3fv(verticies[1])
        glTexCoord2f(1.0, 0.0)
        glVertex3fv(verticies[0])
        
        # # Face Droite 
        glTexCoord2f(1.0, 0.0)
        glVertex3fv(verticies[7])
        glTexCoord2f(1.0, 1.0)
        glVertex3fv(verticies[6])
        glTexCoord2f(0.0, 1.0)
        glVertex3fv(verticies[2])
        glTexCoord2f(0.0, 0.0)
        glVertex3fv(verticies[1])
        
        # # Face Gauche
        glTexCoord2f(0.0, 0.0)
        glVertex3fv(verticies[4])       
        glTexCoord2f(1.0, 0.0)
        glVertex3fv(verticies[0])       
        glTexCoord2f(1.0, 1.0)
        glVertex3fv(verticies[3])      
        glTexCoord2f(0.0, 1.0)
        glVertex3fv(verticies[5])
        
        glEnd()

def draw_text(text, x, y, z):
    font = pygame.font.Font("police/explore.ttf", 24)  # Sélectionnez la police et la taille souhaitées
    text_surface = font.render(text, False, (255, 255, 255))  # Couleur du texte: blanc
    # text_surface.fill((0, 0, 0))  # Définir le fond en bleu
    text_surface.set_colorkey((0, 0, 0))  # Définir la couleur noire comme transparente
    # text_surface.set_colorkey((255, 0, 0))
    text_data = pygame.image.tostring(text_surface, "RGBA", True)

    glPushMatrix()
    glRasterPos3f(x, y, z)
    glDrawPixels(text_surface.get_width(), text_surface.get_height(), GL_RGBA, GL_UNSIGNED_BYTE, text_data)
    glPopMatrix()
    
def init_lighting():
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)

    light_position = [1.0, 1.0, 1.0, 0.0]  # Position de la lumière
    light_color = [1.0, 1.0, .5, 1.0]     # Couleur de la lumière

    glLightfv(GL_LIGHT0, GL_POSITION, light_position)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, light_color)

def main():
    pygame.init()
    display = (800,600)
    fenetre_pygame = pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    fenetre_pygame.fill((255, 255, 255))  # couleur de fond pygame

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    glEnable(GL_DEPTH_TEST)
    glEnable(GL_NORMALIZE)
    glEnable(GL_COLOR_MATERIAL)

    glTranslatef(0.0,0.0, -5)
    # init_lighting()
    loadTexture()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        glRotatef(0.5, 3, 1, 1)
        
        cube(size=0.5)
        cube((.5,.5,.5), 0.7)
        cube((-.5,-.5,-.5), 0.2)
        draw_text("Toto", -.5, 1.5, -.5)

        pygame.display.flip()
        pygame.time.wait(16)

main()