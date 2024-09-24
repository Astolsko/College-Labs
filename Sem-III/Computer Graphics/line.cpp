#include <graphics.h>
#include <stdio.h>
#include <math.h>

void DDA(int x1, int y1, int x2, int y2) {
    int dx = x2 - x1;
    int dy = y2 - y1;

    int steps = abs(dx) > abs(dy) ? abs(dx) : abs(dy);

    float xIncrement = dx / (float) steps;
    float yIncrement = dy / (float) steps;

    float x = x1;
    float y = y1;

    putpixel(round(x), round(y), WHITE); // Put the initial pixel

    for (int i = 0; i < steps; i++) {
        x += xIncrement;
        y += yIncrement;
        putpixel(round(x), round(y), WHITE); // Round and plot pixel
    }
}

int main() {
    int gd = DETECT, gm;

    // Initialize graphics mode
    initgraph(&gd, &gm, "");

    // Hardcoded coordinates for the line
    int x1 = 100, y1 = 100;
    int x2 = 200, y2 = 200;

    // Call the DDA function to draw the line
    DDA(x1, y1, x2, y2);

    // Hold the screen until a key is pressed
    getch();

    // Close the graphics mode
    closegraph();

    return 0;
}
