#include <graphics.h>
#include <stdio.h>

void drawCircle(int xc, int yc, int x, int y) {
    putpixel(xc + x, yc + y, WHITE); // Octant 1
    putpixel(xc - x, yc + y, WHITE); // Octant 2
    putpixel(xc + x, yc - y, WHITE); // Octant 3
    putpixel(xc - x, yc - y, WHITE); // Octant 4
    putpixel(xc + y, yc + x, WHITE); // Octant 5
    putpixel(xc - y, yc + x, WHITE); // Octant 6
    putpixel(xc + y, yc - x, WHITE); // Octant 7
    putpixel(xc - y, yc - x, WHITE); // Octant 8
}

void midPointCircle(int xc, int yc, int r) {
    int x = 0, y = r;
    int d = 1 - r; // Initial decision parameter

    drawCircle(xc, yc, x, y);

    while (x <= y) {
        x++;

        // Decision parameter update
        if (d < 0) {
            d = d + 2 * x + 1;
        } else {
            y--;
            d = d + 2 * (x - y) + 1;
        }

        drawCircle(xc, yc, x, y);
    }
}

int main() {
    int gd = DETECT, gm;

    initgraph(&gd, &gm, "");

    int xc = 200, yc = 200; // Center of the circle
    int radius = 100;       // Radius of the circle

    midPointCircle(xc, yc, radius);

    getch();
    closegraph();

    return 0;
}
