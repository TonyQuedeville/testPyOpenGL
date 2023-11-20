import sys
import OpenGL.GL as gl
import OpenGL.GLUT as glut

def display():
    gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)
    gl.glLoadIdentity()
    gl.glTranslatef(0.0, 0.0, 7.0)

    gl.glRotatef(60, 1, 1, 0)  # Rotation autour de l'axe x et y

    # Cube
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
    
    glut.glutSwapBuffers()

def close_callback():
    sys.exit(0)

def main():
    glut.glutInit(sys.argv)
    glut.glutInitDisplayMode(glut.GLUT_DOUBLE | glut.GLUT_RGB | glut.GLUT_DEPTH)
    glut.glutInitWindowSize(400, 400)
    glut.glutCreateWindow(b"Cube OpenGL Example")
    gl.glEnable(gl.GL_DEPTH_TEST)  # Activation du test de profondeur pour que les faces avant du cube apparaissent et non dans l'ordre défini du code
    gl.glClearColor(0.0, 0.0, 0.0, 1.0)
    gl.glMatrixMode(gl.GL_PROJECTION)
    gl.glLoadIdentity()
    gl.glOrtho(-2, 2, -2, 2, -10, 10)
    gl.glMatrixMode(gl.GL_MODELVIEW)
    glut.glutDisplayFunc(display)
    glut.glutCloseFunc(close_callback)
    glut.glutMainLoop()

if __name__ == "__main__":
    main()