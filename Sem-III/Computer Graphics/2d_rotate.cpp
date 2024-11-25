#include <graphics.h>
#include <cmath>
#include <conio.h>

// Function to rotate a triangle around a pivot point
void rotateTriangle(int x1, int y1, int x2, int y2, int x3, int y3, int angle, int px, int py)
{
    // Convert angle to radians
    float radian = angle * M_PI / 180.0;

    // Rotate each point around the pivot (px, py)
    int nx1 = px + (x1 - px) * cos(radian) - (y1 - py) * sin(radian);
    int ny1 = py + (x1 - px) * sin(radian) + (y1 - py) * cos(radian);
    int nx2 = px + (x2 - px) * cos(radian) - (y2 - py) * sin(radian);
    int ny2 = py + (x2 - px) * sin(radian) + (y2 - py) * cos(radian);
    int nx3 = px + (x3 - px) * cos(radian) - (y3 - py) * sin(radian);
    int ny3 = py + (x3 - px) * sin(radian) + (y3 - py) * cos(radian);

    // Draw the rotated triangle
    line(nx1, ny1, nx2, ny2);
    line(nx2, ny2, nx3, ny3);
    line(nx3, ny3, nx1, ny1);
}

int main()
{
    int gd = DETECT, gm;
    initgraph(&gd, &gm, "");

    // Coordinates of the triangle vertices
    int x1 = 200, y1 = 200;
    int x2 = 300, y2 = 200;
    int x3 = 250, y3 = 300;

    // Pivot point for rotation (center of the triangle)
    int px = (x1 + x2 + x3) / 3;
    int py = (y1 + y2 + y3) / 3;

    // Draw the original triangle in white
    setcolor(WHITE);
    line(x1, y1, x2, y2);
    line(x2, y2, x3, y3);
    line(x3, y3, x1, y1);

    // Start rotating the triangle
    int previousAngle = 0;
    for (int angle = 0; angle <= 360; angle++)
    {
        // Clear the previous triangle by drawing it in the background color (BLACK)
        setcolor(BLACK);
        rotateTriangle(x1, y1, x2, y2, x3, y3, previousAngle, px, py);

        // Draw the rotated triangle in white
        setcolor(WHITE);
        rotateTriangle(x1, y1, x2, y2, x3, y3, angle, px, py);

        // Update the previous angle and introduce a delay for animation
        previousAngle = angle;
        delay(50);
    }

    getch();
    closegraph();
    return 0;
}