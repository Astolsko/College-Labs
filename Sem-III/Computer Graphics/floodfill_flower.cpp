#include <graphics.h>
#include <cmath>

// Midpoint circle algorithm to draw a circle
void drawCircle(int x0, int y0, int radius, int color) {
    int x = radius, y = 0;
    int decisionOver2 = 1 - x;   // Decision criterion for the midpoint

    while (y <= x) {
        // Plotting the points in all octants
        putpixel(x0 + x, y0 + y, color);
        putpixel(x0 + y, y0 + x, color);
        putpixel(x0 - x, y0 + y, color);
        putpixel(x0 - y, y0 + x, color);
        putpixel(x0 - x, y0 - y, color);
        putpixel(x0 - y, y0 - x, color);
        putpixel(x0 + x, y0 - y, color);
        putpixel(x0 + y, y0 - x, color);

        y++;
        if (decisionOver2 <= 0) {
            decisionOver2 += 2 * y + 1; // Midpoint inside, move east
        } else {
            x--;
            decisionOver2 += 2 * (y - x) + 1; // Midpoint outside, move southeast
        }
    }
}

// 4-connected flood fill algorithm
void floodFill4(int x, int y, int fillColor, int boundaryColor) {
    if (getpixel(x, y) != boundaryColor && getpixel(x, y) != fillColor) {
        putpixel(x, y, fillColor);
        floodFill4(x + 1, y, fillColor, boundaryColor);
        floodFill4(x - 1, y, fillColor, boundaryColor);
        floodFill4(x, y + 1, fillColor, boundaryColor);
        floodFill4(x, y - 1, fillColor, boundaryColor);
    }
}

// Draw a flower with a center and surrounding petals
void drawFlower(int centerX, int centerY, int radius) {
    
    // Draw and fill the petals
    int petalRadius = radius;
    
    for (int i = 0; i < 5; i++) {
        double radians = (72 * i) * M_PI / 180.0; // Angle for each petal
        int x = centerX + petalRadius * cos(radians);
        int y = centerY + petalRadius * sin(radians);
        drawCircle(x, y, radius, YELLOW);
        floodFill4(x, y, YELLOW, WHITE); // Fill each petal
    }
    // Draw and fill the center circle
    drawCircle(centerX, centerY, radius / 2, RED);
    floodFill4(centerX, centerY, RED, BLACK); // Fill the center circle

}

int main() {
    int gd = DETECT, gm;
    initgraph(&gd, &gm, ""); // Initialize graphics

    // Set background color
    setbkcolor(BLACK);
    cleardevice();

    drawFlower(200, 200, 50); // Draw flower at (200, 200) with radius 50

    getch();
    closegraph();
    return 0;
}
