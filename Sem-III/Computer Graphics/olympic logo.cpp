#include <graphics.h>
#include <stdio.h>

void drawCircle(int xc, int yc, int x, int y, int color) {
    putpixel(xc + x, yc + y, color);
    putpixel(xc - x, yc + y, color);
    putpixel(xc + x, yc - y, color);
    putpixel(xc - x, yc - y, color);
    putpixel(xc + y, yc + x, color);
    putpixel(xc - y, yc + x, color);
    putpixel(xc + y, yc - x, color);
    putpixel(xc - y, yc - x, color);
}

void midPointCircle(int xc, int yc, int r, int color) {
    int x = 0, y = r;
    int d = 1 - r; // Initial decision parameter

    drawCircle(xc, yc, x, y, color);

    while (x <= y) {
        x++;

        if (d < 0) {
            d = d + 2 * x + 1;
        } else {
            y--;
            d = d + 2 * (x - y) + 1;
        }

        drawCircle(xc, yc, x, y, color);
    }
}

int main() {
    int gd = DETECT, gm;
    initgraph(&gd, &gm, "");

    // Circle radius and positions
    int radius = 80;

    // Coordinates for the top three circles (Blue, White (instead of Black), Red)
    int xc1 = 200, yc1 = 200;  // Blue
    int xc2 = 350, yc2 = 200;  // White (instead of Black)
    int xc3 = 500, yc3 = 200;  // Red

    // Coordinates for the bottom two circles (Yellow, Green)
    int xc4 = 275, yc4 = 280;  // Yellow
    int xc5 = 425, yc5 = 280;  // Green

    // Draw the circles using the Mid-Point Circle Algorithm
    midPointCircle(xc1, yc1, radius, BLUE);    // Blue circle
    midPointCircle(xc2, yc2, radius, WHITE);   // White circle (instead of Black)
    midPointCircle(xc3, yc3, radius, RED);     // Red circle
    midPointCircle(xc4, yc4, radius, YELLOW);  // Yellow circle
    midPointCircle(xc5, yc5, radius, GREEN);   // Green circle

    getch();
    closegraph();

    return 0;
}
