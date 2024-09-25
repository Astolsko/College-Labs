#include <graphics.h>
#include <stdio.h>
#include <conio.h>

void bresenhamLine(int x1, int y1, int x2, int y2) {
    int dx, dy, p, x, y;

    dx = x2 - x1;
    dy = y2 - y1;

    x = x1;
    y = y1;

    // For vertical line (slope 90 degrees), dx is 0
    if (dx == 0) {
        while (y <= y2) {
            putpixel(x, y, WHITE); // Drawing the pixel
            y++;
        }
    }
}

int main() {
    int gd = DETECT, gm;

    // Initialize graphics mode
    initgraph(&gd, &gm, "C:\\TURBOC3\\BGI");

    // Hardcoded coordinates for the vertical line (slope 90 degrees)
    int x1 = 200, y1 = 100; // Start point
    int x2 = 200, y2 = 300; // End point (same x, different y)

    // Call function to draw the vertical line
    bresenhamLine(x1, y1, x2, y2);

    getch();
    closegraph(); // Close graphics mode

    return 0;
}
