import numpy as np
import sys
import math
import OpenGL.GL as gl
import OpenGL.GLUT as glut

# -------------------------------------------------------------------------------------------------------------------

# Formes géométriques

def sphere():
    gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)
    gl.glLoadIdentity()
    gl.glTranslatef(0.0, 0.0, -10.0)

    slices = 50  # Diviser la sphère en "tranches"
    stacks = 50  # Diviser la sphère en "piles"

    for i in range(stacks):
        lat0 = math.pi * (-0.5 + (i / stacks))
        z0 = math.sin(lat0)
        zr0 = math.cos(lat0)

        lat1 = math.pi * (-0.5 + ((i + 1) / stacks))
        z1 = math.sin(lat1)
        zr1 = math.cos(lat1)

        # Dessiner les "tranches" de la sphère
        gl.glBegin(gl.GL_QUAD_STRIP)
        for j in range(slices + 1):
            lng = 2 * math.pi * (j / slices)
            x = math.cos(lng)
            y = math.sin(lng)

            gl.glNormal3f(x * zr0, y * zr0, z0)
            gl.glVertex3f(x * zr0, y * zr0, z0)

            gl.glNormal3f(x * zr1, y * zr1, z1)
            gl.glVertex3f(x * zr1, y * zr1, z1)
        gl.glEnd()
    
def cube():
    gl.glTranslatef(.0, .0, -10.)
    gl.glRotatef(60, 1, 1, 0)

    gl.glBegin(gl.GL_QUADS)

    gl.glColor3f(1.0, 0.0, 0.0)  # Face rouge
    gl.glVertex3f(1.0, 1.0, -1.0)
    gl.glVertex3f(-1.0, 1.0, -1.0)
    gl.glVertex3f(-1.0, 1.0, 1.0)
    gl.glVertex3f(1.0, 1.0, 1.0)

    gl.glColor3f(0.0, 1.0, 0.0)  # Face verte
    gl.glVertex3f(1.0, -1.0, 1.0)
    gl.glVertex3f(-1.0, -1.0, 1.0)
    gl.glVertex3f(-1.0, -1.0, -1.0)
    gl.glVertex3f(1.0, -1.0, -1.0)

    gl.glColor3f(0.0, 0.0, 1.0)  # Face bleue
    gl.glVertex3f(1.0, 1.0, 1.0)
    gl.glVertex3f(-1.0, 1.0, 1.0)
    gl.glVertex3f(-1.0, -1.0, 1.0)
    gl.glVertex3f(1.0, -1.0, 1.0)

    gl.glColor3f(1.0, 1.0, 0.0)  # Face jaune
    gl.glVertex3f(1.0, -1.0, -1.0)
    gl.glVertex3f(-1.0, -1.0, -1.0)
    gl.glVertex3f(-1.0, 1.0, -1.0)
    gl.glVertex3f(1.0, 1.0, -1.0)

    gl.glColor3f(1.0, 0.0, 1.0)  # Face magenta
    gl.glVertex3f(-1.0, 1.0, 1.0)
    gl.glVertex3f(-1.0, 1.0, -1.0)
    gl.glVertex3f(-1.0, -1.0, -1.0)
    gl.glVertex3f(-1.0, -1.0, 1.0)

    gl.glColor3f(0.0, 1.0, 1.0)  # Face cyan
    gl.glVertex3f(1.0, 1.0, -1.0)
    gl.glVertex3f(1.0, 1.0, 1.0)
    gl.glVertex3f(1.0, -1.0, 1.0)
    gl.glVertex3f(1.0, -1.0, -1.0)
    
    gl.glEnd()

# ----------------------------------------------------------------------------------------------------

# Scene

def gluPerspective(fovy, aspect, near, far):
    f = 1.0 / np.tan(np.radians(fovy) / 2.0)
    projection_matrix = np.array([
        [f / aspect, 0, 0, 0],
        [0, f, 0, 0],
        [0, 0, (far + near) / (near - far), (2 * far * near) / (near - far)],
        [0, 0, -1, 0]
    ], dtype=np.float32)
    gl.glMatrixMode(gl.GL_PROJECTION)
    gl.glLoadIdentity()
    gl.glMultMatrixf(projection_matrix.T)

def display():
    gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)
    gl.glLoadIdentity()
    gluPerspective(45, 1, 0.1, 100)  # Utilisation de la perspective
    
    # cube()
    sphere()

    glut.glutSwapBuffers()

def main():
    glut.glutInit(sys.argv)
    glut.glutInitDisplayMode(glut.GLUT_DOUBLE | glut.GLUT_RGB | glut.GLUT_DEPTH)
    glut.glutInitWindowSize(600, 600)
    glut.glutCreateWindow(b"Perspective OpenGL Example")
    gl.glEnable(gl.GL_DEPTH_TEST)  # Activation du test de profondeur pour que les faces avant du cube apparaissent et non dans l'ordre défini du code
    gl.glClearColor(0.0, 0.0, 0.0, 1.0)
    gl.glMatrixMode(gl.GL_PROJECTION)
    gl.glLoadIdentity()
    gl.glMatrixMode(gl.GL_MODELVIEW)
    glut.glutDisplayFunc(display)
    glut.glutMainLoop()

if __name__ == "__main__":
    main()
