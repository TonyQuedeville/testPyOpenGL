# Initiation à pyOpenGl

# pip install PyOpenGL
# pip install PyOpenGL PyOpenGL_accelerate


import sys

import OpenGL.GL as gl
import OpenGL.GLUT as glut

def display():
    gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)
    gl.glLoadIdentity()
    gl.glTranslatef(0.0, 0.0, -5.0)

    gl.glBegin(gl.GL_TRIANGLES)
    gl.glColor3f(1.0, 0.0, 0.0)
    gl.glVertex3f(0.0, 1.0, 0.0)
    gl.glColor3f(0.0, 1.0, 0.0)
    gl.glVertex3f(-1.0, -1.0, 0.0)
    gl.glColor3f(0.0, 0.0, 1.0)
    gl.glVertex3f(1.0, -1.0, 0.0)
    gl.glEnd()

    glut.glutSwapBuffers()

def main():
    glut.glutInit(sys.argv)
    glut.glutInitDisplayMode(glut.GLUT_DOUBLE | glut.GLUT_RGB | glut.GLUT_DEPTH)
    glut.glutInitWindowSize(400, 400)
    glut.glutCreateWindow(b"Simple OpenGL Example")
    gl.glClearColor(0.0, 0.0, 0.0, 1.0)
    gl.glMatrixMode(gl.GL_PROJECTION)
    gl.glLoadIdentity()
    gl.glOrtho(-2, 2, -2, 2, -10, 10)
    gl.glMatrixMode(gl.GL_MODELVIEW)
    glut.glutDisplayFunc(display)
    glut.glutMainLoop()

if __name__ == "__main__":
    main()
