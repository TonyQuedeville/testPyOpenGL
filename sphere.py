import OpenGL.GL as gl
import OpenGL.GLUT as glut
import OpenGL.GLU as glu
import math

# Position et couleur de la lumière
light_position = [1.0, 1.0, 1.0, 0.0]
light_ambient = [0.2, 0.2, 0.2, 1.0]
light_diffuse = [1.0, 1.0, 1.0, 1.0]
light_specular = [.5, .5, .5, 1.0]

def init_light():
    gl.glLightfv(gl.GL_LIGHT0, gl.GL_POSITION, light_position)
    gl.glLightfv(gl.GL_LIGHT0, gl.GL_AMBIENT, light_ambient)
    gl.glLightfv(gl.GL_LIGHT0, gl.GL_DIFFUSE, light_diffuse)
    gl.glLightfv(gl.GL_LIGHT0, gl.GL_SPECULAR, light_specular)
    gl.glEnable(gl.GL_LIGHTING)
    gl.glEnable(gl.GL_LIGHT0)
    gl.glEnable(gl.GL_DEPTH_TEST)
    gl.glShadeModel(gl.GL_SMOOTH)

def display():
    gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)
    gl.glLoadIdentity()
    gl.glTranslatef(0.0, 0.0, -5.0)

    glut.glutSolidSphere(1, 50, 50)  # Dessine une sphère de rayon 1

    glut.glutSwapBuffers()

def reshape(width, height):
    gl.glViewport(0, 0, width, height)
    gl.glMatrixMode(gl.GL_PROJECTION)
    gl.glLoadIdentity()
    glu.gluPerspective(45, (width / height), 0.1, 100.0)
    gl.glMatrixMode(gl.GL_MODELVIEW)

def main():
    glut.glutInit()
    glut.glutInitDisplayMode(glut.GLUT_DOUBLE | glut.GLUT_RGB | glut.GLUT_DEPTH)
    glut.glutInitWindowSize(400, 400)
    glut.glutCreateWindow(b"Sphere OpenGL Example")
    gl.glClearColor(0.0, 0.0, 0.0, 1.0)
    gl.glEnable(gl.GL_DEPTH_TEST)
    init_light()
    glut.glutDisplayFunc(display)
    glut.glutReshapeFunc(reshape)
    glut.glutMainLoop()

if __name__ == "__main__":
    main()
