#include <GL/glut.h>  // Include the GLUT header

// Initial scaling factors
float scaleX = 1.0f, scaleY = 1.0f, scaleZ = 1.0f;

// Function to draw a cube
void drawCube() {
    glBegin(GL_QUADS);

    // Front face
    glColor3f(1.0, 0.0, 0.0);  // Red
    glVertex3f(-0.5, -0.5,  0.5);
    glVertex3f( 0.5, -0.5,  0.5);
    glVertex3f( 0.5,  0.5,  0.5);
    glVertex3f(-0.5,  0.5,  0.5);

    // Back face
    glColor3f(0.0, 1.0, 0.0);  // Green
    glVertex3f(-0.5, -0.5, -0.5);
    glVertex3f(-0.5,  0.5, -0.5);
    glVertex3f( 0.5,  0.5, -0.5);
    glVertex3f( 0.5, -0.5, -0.5);

    // Top face
    glColor3f(0.0, 0.0, 1.0);  // Blue
    glVertex3f(-0.5,  0.5, -0.5);
    glVertex3f(-0.5,  0.5,  0.5);
    glVertex3f( 0.5,  0.5,  0.5);
    glVertex3f( 0.5,  0.5, -0.5);

    // Bottom face
    glColor3f(1.0, 1.0, 0.0);  // Yellow
    glVertex3f(-0.5, -0.5, -0.5);
    glVertex3f( 0.5, -0.5, -0.5);
    glVertex3f( 0.5, -0.5,  0.5);
    glVertex3f(-0.5, -0.5,  0.5);

    // Right face
    glColor3f(1.0, 0.0, 1.0);  // Magenta
    glVertex3f( 0.5, -0.5, -0.5);
    glVertex3f( 0.5,  0.5, -0.5);
    glVertex3f( 0.5,  0.5,  0.5);
    glVertex3f( 0.5, -0.5,  0.5);

    // Left face
    glColor3f(0.0, 1.0, 1.0);  // Cyan
    glVertex3f(-0.5, -0.5, -0.5);
    glVertex3f(-0.5, -0.5,  0.5);
    glVertex3f(-0.5,  0.5,  0.5);
    glVertex3f(-0.5,  0.5, -0.5);

    glEnd();
}

// Display function
void display() {
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
    glLoadIdentity();

    // Apply scaling
    glScalef(scaleX, scaleY, scaleZ);

    // Draw the cube
    drawCube();

    glutSwapBuffers();
}

// Keyboard function to adjust scaling factors
void keyboard(unsigned char key, int x, int y) {
    switch (key) {
        case 'x':
            scaleX += 0.1f; // Increase scale in X
            scaleY += 0.1f; // Increase scale in Y
            scaleZ += 0.1f; // Increase scale in Z
            break;
        case 'r': scaleX = scaleY = scaleZ = 1.0f; break;  // Reset scaling
    }
    glutPostRedisplay();
}

// Initialize OpenGL
void init() {
    glEnable(GL_DEPTH_TEST);  // Enable depth testing
}

// Main function
int main(int argc, char** argv) {
    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH);
    glutInitWindowSize(800, 600);
    glutCreateWindow("Scaling a Cube");

    init();

    glutDisplayFunc(display);
    glutKeyboardFunc(keyboard);

    glutMainLoop();
    return 0;
}
