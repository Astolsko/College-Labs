#include <graphics.h>
#include <conio.h>
#include <stdio.h>
void plotEllipsePoints(int xc, int yc, int x, int y)
{
    putpixel(xc + x, yc + y, WHITE);
    putpixel(xc - x, yc + y, WHITE);
    putpixel(xc + x, yc - y, WHITE);
    putpixel(xc - x, yc - y, WHITE);
}
void drawEllipse(int xc, int yc, int a, int b)
{
    int x = 0;
    int y = b;
    int p1 = b * b - a * a * b + a * a / 4;
    while (2 * b * b * x <= 2 * a * a * y)
    {
        plotEllipsePoints(xc, yc, x, y);
        if (p1 < 0)
        {
            p1 = p1 + 2 * b * b * x + b * b;
        }
        else
        {
            p1 = p1 + 2 * b * b * x - 2 * a * a * y + b * b;
            y--;
        }
        x++;
    }
    int p2 = b * b * (x + 1) * (x + 1) + a * a * (y - 1) * (y - 1) - a * a * b * b;
    while (y >= 0)
    {
        plotEllipsePoints(xc, yc, x, y);
        if (p2 > 0)
        {
            p2 = p2 - 2 * a * a * y + a * a;
        }
        else
        {
            p2 = p2 + 2 * b * b * x + b * b - 2 * a * a * y;
            x++;
        }
        y--;
    }
}

#include <graphics.h> // Include the graphics header file
#include <conio.h>   // For getch() (to wait for a key press)


int main() {
    int gd = DETECT, gm; // gd: graphics driver, gm: graphics mode. DETECT automatically detects the graphics driver.

    initgraph(&gd, &gm, ""); // Initialize the graphics system.  The "" is for the path to the BGI driver.

    drawEllipse(150, 150, 100, 50); // Draws an ellipse.  Parameters are: center x, center y, horizontal radius, vertical radius.
    drawEllipse(150, 150, 20, 50);  // Draws a thinner, taller ellipse at the same center.
    drawEllipse(150, 123, 75, 22);  // Draws a smaller ellipse at a slightly different position.


    getch();      // Waits for a key press before closing the graphics window.
    closegraph(); // Closes the graphics mode.

    return 0;     // Indicates successful execution.
}