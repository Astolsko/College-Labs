#include <graphics.h>
#include <stdio.h>
#include <conio.h>
#include <stdlib.h>

void drawCar(int x, int y) {
    // Car body
    setcolor(BLUE); // Set car outline color to blue
    rectangle(x, y, x + 100, y + 50);           // Main body
    rectangle(x + 20, y - 20, x + 80, y);       // Car roof
    setfillstyle(SOLID_FILL, BLUE);             // Set fill color to blue
    floodfill(x + 1, y + 1, BLUE);              // Fill car body
    floodfill(x + 21, y - 1, BLUE);             // Fill car roof

    // Wheels
    setcolor(WHITE);  // Set wheel outline color to white
    circle(x + 20, y + 50, 15);                 // Left wheel
    circle(x + 80, y + 50, 15);                 // Right wheel
    setfillstyle(SOLID_FILL, BLACK);            // Fill wheels with black
    floodfill(x + 20, y + 51, WHITE);           // Fill left wheel
    floodfill(x + 80, y + 51, WHITE);           // Fill right wheel
}

void drawSmoke(int x, int y, int size) {
    setcolor(LIGHTGRAY);  // Set smoke color
    circle(x, y, size);   // Smoke circles
    setfillstyle(SOLID_FILL, LIGHTGRAY);
    floodfill(x, y, LIGHTGRAY);
}

int main() {
    int gd = DETECT, gm;
    initgraph(&gd, &gm, "");

    // Set background color to white
    setbkcolor(WHITE);
    cleardevice();        // Clear the screen with the background color

    int x = 50, y = 300;  // Initial position of the car
    int smokeX, smokeY;   // Smoke coordinates
    int smokeSize = 5;    // Initial smoke size

    while (x < getmaxx() - 100) {
        cleardevice();    // Clear screen for each frame

        // Draw the car at the new position
        drawCar(x, y);

        // Generate random smoke behind the car's exhaust
        smokeX = x - 10;              // Smoke starts behind the car
        smokeY = y + 20 + rand() % 20;  // Random vertical position for smoke
        smokeSize = 5 + rand() % 10;    // Random size for smoke

        // Draw smoke that moves up and grows
        drawSmoke(smokeX, smokeY - 10, smokeSize);        // First smoke puff
        drawSmoke(smokeX - 15, smokeY - 30, smokeSize + 5); // Second smoke puff
        drawSmoke(smokeX - 30, smokeY - 50, smokeSize + 10); // Third smoke puff

        delay(50);       // Pause to control the speed of the car movement

        x += 5;          // Move the car to the right by 5 pixels
    }

    getch();
    closegraph();

    return 0;
}
