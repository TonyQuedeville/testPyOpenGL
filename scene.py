import OpenGL.GL as gl
import OpenGL.GLUT as glut
import OpenGL.GLU as glu
import math

# Position et orientation de la caméra
camera_position = [0.0, 0.0, 8.0]
look_at_position = [0.0, 0.0, 0.0]
up_vector = [0.0, 1.0, 0.0]
# Ajoutez une variable pour stocker les positions de la caméra
camera_yaw = 0.0
camera_pitch = 0.0
last_x, last_y = 0, 0

# Position Formes
sphere_position = [-2.0, 0.0, 0.0]
cube_position = [2.0, 0.0, 0.0]
tetrahedre_position = [0.0, 2.0, 0.0]

# Position et couleur de la lumière
light_position = [1.0, 1.0, 1.0, 0.0]
light_ambient = [0.0, 0.5, 0.5, 1.0]
light_diffuse = [0.8, 0.8, 0.8, 1.0]
light_specular = [0.8, 0.8, 0.8, 1.0]

def init_light():
    gl.glLightfv(gl.GL_LIGHT0, gl.GL_POSITION, light_position)
    gl.glLightfv(gl.GL_LIGHT0, gl.GL_AMBIENT, light_ambient)
    gl.glLightfv(gl.GL_LIGHT0, gl.GL_DIFFUSE, light_diffuse)
    gl.glLightfv(gl.GL_LIGHT0, gl.GL_SPECULAR, light_specular)
    gl.glEnable(gl.GL_LIGHTING)
    gl.glEnable(gl.GL_LIGHT0)
    gl.glEnable(gl.GL_DEPTH_TEST)
    gl.glShadeModel(gl.GL_SMOOTH)

def draw_objects():
    # Sphère
    gl.glPushMatrix()
    gl.glTranslatef(*sphere_position)
    gl.glColor3f(1.,1.,0.)
    glut.glutSolidSphere(1, 50, 50)
    gl.glPopMatrix()

    # Cube
    gl.glPushMatrix()
    gl.glTranslatef(*cube_position)
    gl.glColor3f(1.,0.,0.)
    glut.glutSolidCube(1)
    gl.glPopMatrix()

    # Tétraèdre
    gl.glPushMatrix()
    gl.glTranslatef(*tetrahedre_position)
    gl.glColor3f(0.,0.,1.)
    glut.glutSolidTetrahedron()
    gl.glPopMatrix()

    # Plan
    gl.glPushMatrix()
    gl.glTranslatef(0.0, -2.0, 0.0)
    gl.glScalef(10.0, 0.1, 10.0)  # Ajuster la taille du plan
    gl.glColor3f(0.2,0.2,0.2)
    glut.glutSolidCube(1)  # Utiliser un cube pour représenter le plan
    gl.glPopMatrix()

def display():
    gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)
    gl.glLoadIdentity()
    gl.glTranslatef(0.0, 0.0, -8.0)
    
    # Appliquez les transformations de la caméra
    gl.glRotatef(camera_pitch, 1.0, 0.0, 0.0)
    gl.glRotatef(camera_yaw, 0.0, 1.0, 0.0)
    gl.glTranslatef(0.0, 0.0, -5.0)

    draw_objects()

    glut.glutSwapBuffers()

def mouse_click(button, state, x, y):
    global last_x, last_y
    if button == glut.GLUT_LEFT_BUTTON and state == glut.GLUT_DOWN:
        # Capture le clic gauche pour activer le mouvement de la caméra
        last_x, last_y = x, y

def mouse_motion(x, y):
    global last_x, last_y, camera_yaw, camera_pitch, sensitivity    
    dx = x - last_x 
    dy = y - last_y 
    
    last_x, last_y = x, y

    sensitivity = 0.1  # Ajustez la sensibilité selon votre besoin
    camera_yaw += dx * sensitivity
    camera_pitch += dy * sensitivity

    glut.glutPostRedisplay()  # Demande une nouvelle mise à jour de l'affichage

def special_keys(key, x, y):
    global sphere_position, cube_position, tetrahedre_position

    # Déplacer la caméra en fonction des touches spéciales
    modifiers = glut.glutGetModifiers()
    yz = 1  # Valeur par défaut si aucune touche spéciale n'est activée
    step_size = 1.0  # Valeur par défaut pour step_size
    
    if modifiers == (glut.GLUT_ACTIVE_CTRL | glut.GLUT_ACTIVE_SHIFT): # Les deux touches sont activées en même temps
        step_size = 0.1  
        yz = 2 
    elif modifiers == glut.GLUT_ACTIVE_CTRL: # Seulement la touche CTRL est activée
        yz = 2  
        step_size = 1.0
    elif modifiers == glut.GLUT_ACTIVE_SHIFT: # Seulement la touche SHIFT est activée
        yz = 1  
        step_size = 0.1
    else:
        yz = 1
        step_size = 1.0
    
    if key == glut.GLUT_KEY_LEFT:
        sphere_position[0] -= step_size
        cube_position[0] -= step_size
        tetrahedre_position[0] -= step_size
    elif key == glut.GLUT_KEY_RIGHT:
        sphere_position[0] += step_size
        cube_position[0] += step_size
        tetrahedre_position[0] += step_size
    elif key == glut.GLUT_KEY_UP:
        sphere_position[yz] += step_size
        cube_position[yz] += step_size
        tetrahedre_position[yz] += step_size
    elif key == glut.GLUT_KEY_DOWN:
        sphere_position[yz] -= step_size
        cube_position[yz] -= step_size
        tetrahedre_position[yz] -= step_size

    glut.glutPostRedisplay()


def reshape(width, height):
    gl.glViewport(0, 0, width, height)
    gl.glMatrixMode(gl.GL_PROJECTION)
    gl.glLoadIdentity()
    glu.gluPerspective(60, (width / height), 0.1, 100.0)
    gl.glMatrixMode(gl.GL_MODELVIEW)

def main():
    glut.glutInit()
    glut.glutInitDisplayMode(glut.GLUT_DOUBLE | glut.GLUT_RGB | glut.GLUT_DEPTH)
    glut.glutInitWindowSize(800, 600)
    glut.glutCreateWindow(b"Multiple Objects OpenGL Example")
    gl.glEnable(gl.GL_DEPTH_TEST)
    init_light()
    gl.glClearColor(0.0, 0.0, 0.1, 1.0) # couleur de fond
    glut.glutDisplayFunc(display)
    glut.glutReshapeFunc(reshape)
    glut.glutSpecialFunc(special_keys)  # Gestion clavier
    glut.glutMotionFunc(mouse_motion)
    glut.glutMouseFunc(mouse_click)
    glut.glutMainLoop()

if __name__ == "__main__":
    main()
