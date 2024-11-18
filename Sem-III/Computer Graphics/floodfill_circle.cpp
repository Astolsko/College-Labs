#include <graphics.h>
#include <conio.h>
#include <stdio.h>
void floodFill(int x, int y, int fillColor, int borderColor)
{
    int currentColor = getpixel(x, y);
    if (currentColor != borderColor && currentColor != fillColor)
    {
        putpixel(x, y, fillColor);
        floodFill(x + 1, y, fillColor, borderColor); // Right
        floodFill(x - 1, y, fillColor, borderColor); // Left
        floodFill(x, y + 1, fillColor, borderColor); // Down
        floodFill(x, y - 1, fillColor, borderColor); // Up
    }
}
int main()
{
    int gd = DETECT, gm;
    initgraph(&gd, &gm, "");
    setbkcolor(WHITE);
    cleardevice();
    setcolor(RED);
    circle(300, 300, 100);          // Draw a circle with center (300, 300) and radius 100
    floodFill(300, 300, BLUE, RED); // Fill the circle with BLUE color (inside) and RED as
    getch();
    closegraph();
    return 0;
}