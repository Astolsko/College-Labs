#include <graphics.h>
#include <conio.h>
#include <cmath>
#include <dos.h>
void drawCar(int x, int y, int wheelRotation) {
    // Car Body
    setcolor(YELLOW);
    rectangle(x, y, x + 120, y - 40); // Main body
    rectangle(x + 30, y - 40, x + 90, y - 60); // Top of the car
    floodfill(x + 60, y - 20, YELLOW);

    // Windows
    setcolor(BLUE);
    rectangle(x + 35, y - 55, x + 85, y - 40); // Window
    floodfill(x + 60, y - 47, BLUE);
    // Wheels
    setcolor(BLACK);
    int wheelRadius = 15;
    // Left Wheel
    circle(x + 30, y, wheelRadius);
    setcolor(BLACK);
    circle(x + 30, y, wheelRadius - 5); // Inner rim
    // Right Wheel
    circle(x + 90, y, wheelRadius);
    setcolor(BLACK);
    circle(x + 90, y, wheelRadius - 5); // Inner rim
    setcolor(BLACK);
    line(x + 30 + cos(wheelRotation * M_PI / 180) * wheelRadius,
         y - sin(wheelRotation * M_PI / 180) * wheelRadius,
         x + 30 - cos(wheelRotation * M_PI / 180) * wheelRadius,
         y + sin(wheelRotation * M_PI / 180) * wheelRadius);

    line(x + 90 + cos(wheelRotation * M_PI / 180) * wheelRadius,
         y - sin(wheelRotation * M_PI / 180) * wheelRadius,
         x + 90 - cos(wheelRotation * M_PI / 180) * wheelRadius,
         y + sin(wheelRotation * M_PI / 180) * wheelRadius);
}
void drawSmoke(int x, int y, int frame) {
    // Smoke effect
    int smokeX = x - 20 - frame * 5; // Move smoke to the left
    int smokeY = y - 30 - frame * 3; // Move smoke upwards
    int smokeSize = 10 + frame; // Increase smoke size over time
    if (smokeSize < 30) {
        setcolor(LIGHTGRAY);
        circle(smokeX, smokeY, smokeSize);
        floodfill(smokeX, smokeY, LIGHTGRAY);
    }
}
void drawBackground() {
    // Draw a simple road and sky
    setcolor(CYAN);
    floodfill(0, 0, CYAN); // Sky

    setcolor(GREEN);
    rectangle(0, 300, getmaxx(), getmaxy()); // Grass

    setcolor(DARKGRAY);
    rectangle(0, 280, getmaxx(), 300); // Road
    floodfill(getmaxx()/2, 290, DARKGRAY);
}
int main() {
    int gd = DETECT, gm;
    initgraph(&gd, &gm, "");
    int carX = 50, carY = 300;  // Initial position of the car
    int wheelRotation = 0;      // Angle for rotating wheels
    int frame = 0;              // Smoke animation frame
    while (!kbhit()) { // Loop until a key is pressed
        cleardevice(); // Clear the screen
        drawBackground(); // Draw background
        // Draw moving car
        drawCar(carX, carY, wheelRotation);
        // Draw smoke behind the car
        for (int i = 0; i < 5; i++) {
            drawSmoke(carX - i * 20, carY - 10, (frame + i) % 10);
        }
        // Update car position and wheel rotation
        carX += 5;                // Move car to the right
        wheelRotation += 15;      // Rotate wheels
        frame = (frame + 1) % 10; // Cycle smoke frames

        // Reset position if car reaches the end of the screen
        if (carX > getmaxx()) {
            carX = -120;
        }

        delay(50); // Small delay for smoother animation
    }
    getch();
    closegraph();
    return 0;
}
