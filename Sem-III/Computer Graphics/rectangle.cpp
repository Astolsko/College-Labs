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

    putpixel(round(x), round(y), WHITE);

    for (int i = 0; i < steps; i++) {
        x += xIncrement;
        y += yIncrement;
        putpixel(round(x), round(y), WHITE);
    }
}

int main() {
    int gd = DETECT, gm;

    initgraph(&gd, &gm, "");

    // Hardcoded coordinates for the rectangle
    int x1 = 100, y1 = 100;  // Top-left corner
    int x2 = 250, y2 = 100;  // Top-right corner (wider, making it a rectangle)
    int x3 = 250, y3 = 200;  // Bottom-right corner
    int x4 = 100, y4 = 200;  // Bottom-left corner

    // Draw the rectangle by connecting the four corners
    DDA(x1, y1, x2, y2);  // Top edge
    DDA(x2, y2, x3, y3);  // Right edge
    DDA(x3, y3, x4, y4);  // Bottom edge
    DDA(x4, y4, x1, y1);  // Left edge

    getch();
    closegraph();

    return 0;
}
