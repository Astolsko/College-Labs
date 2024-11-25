#include <GL/glut.h>


void display();

void reshape(int, int);

void init(){
    glClearColor(0.0,0.0,0,1.0);
    glEnable(GL_DEPTH_TEST);
}

void timer(int);

int main(int argc, char**argv){

    glutInit(&argc, argv); // initialized the glut library

    glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE | GLUT_DEPTH); // initialize glut display

    glutInitWindowPosition(200,100);
    glutInitWindowSize(500,500);



    glutCreateWindow("Testing");

    glutDisplayFunc(display);
    glutReshapeFunc(reshape);

    glutTimerFunc(0,timer,0);
    init();

    glutMainLoop();


}
float angle = 0.0;

void display(){

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
    glLoadIdentity();



    // translate before drawing
    glTranslatef(0,0,-8.0);

    // rotate before drawing
    glRotatef(angle,1.0,1.0,1.0);

    // draw
    glBegin(GL_QUADS);

    //front
    glColor3f(1.0,0.0,0.0);
    glVertex3f(-1.0,1.0,1.0);
    glVertex3f(-1.0,-1.0,1.0);
    glVertex3f(1.0,-1.0,1.0);
    glVertex3f(1.0,1.0,1.0);
    //back
    glColor3f(0.0,1.0,0.0);
    glVertex3f(1.0,1.0,-1.0);
    glVertex3f(1.0,-1.0,-1.0);
    glVertex3f(-1.0,-1.0,-1.0);
    glVertex3f(-1.0,1.0,-1.0);
    //right
    glColor3f(0.0,0.0,1.0);
    glVertex3f(1.0,1.0,1.0);
    glVertex3f(1.0,-1.0,1.0);
    glVertex3f(1.0,-1.0,-1.0);
    glVertex3f(1.0,1.0,-1.0);
    //left
    glColor3f(1.0,1.0,0.0);
    glVertex3f(-1.0,1.0,-1.0);
    glVertex3f(-1.0,-1.0,-1.0);
    glVertex3f(-1.0,-1.0,1.0);
    glVertex3f(-1.0,1.0,1.0);
    //top
    glColor3f(0.0,1.0,1.0);
    glVertex3f(-1.0,1.0,-1.0);
    glVertex3f(-1.0,1.0,1.0);
    glVertex3f(1.0,1.0,1.0);
    glVertex3f(1.0,1.0,-1.0);
    //bottom
    glColor3f(1.0,0.0,1.0);
    glVertex3f(-1.0,-1.0,-1.0);
    glVertex3f(-1.0,-1.0,1.0);
    glVertex3f(1.0,-1.0,1.0);
    glVertex3f(1.0,-1.0,-1.0);

    glEnd(); // tells opengl we finished giving vertices and it can start

    glutSwapBuffers(); // swaps the front and back buffers in double buffer mode
}

void reshape(int w, int h){
    // used to set viewport
    glViewport(0,0,(GLsizei) w, (GLsizei) h);

    // used to set projection
    glMatrixMode(GL_PROJECTION);

    glLoadIdentity();
    gluPerspective(60,1,2.0,50.0);
    glMatrixMode(GL_MODELVIEW);
}

void timer(int){

    glutPostRedisplay();
    glutTimerFunc(1000/60, timer,0);

    angle += 0.8;

    if (angle > 360){
        angle -= 360;
    }
}
