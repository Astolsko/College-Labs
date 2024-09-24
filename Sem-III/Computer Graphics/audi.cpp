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
    int d = 1 - r;

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

    // Circle radius and horizontal positions for the Audi logo
    int radius = 80;
    int gap = 20;  // Overlap between circles
    int yc = 200;  // Vertical position of the center of circles

    // X-coordinates for the centers of the four circles
    int xc1 = 150, xc2 = xc1 + 2 * radius - gap;
    int xc3 = xc2 + 2 * radius - gap, xc4 = xc3 + 2 * radius - gap;

    // Draw the four interlocking circles in white (Audi logo)
    midPointCircle(xc1, yc, radius, WHITE);  // First circle
    midPointCircle(xc2, yc, radius, WHITE);  // Second circle
    midPointCircle(xc3, yc, radius, WHITE);  // Third circle
    midPointCircle(xc4, yc, radius, WHITE);  // Fourth circle

    getch();
    closegraph();

    return 0;
}
