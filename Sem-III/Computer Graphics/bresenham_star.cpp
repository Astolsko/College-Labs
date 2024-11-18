#include <graphics.h>
#include <conio.h>
#include <stdio.h>
#include <math.h>


void bresenhamLine(int x1, int y1, int x2, int y2)
{
    int dx = abs(x2 - x1);
    int dy = abs(y2 - y1);
    int sx = (x1 < x2) ? 1 : -1;
    int sy = (y1 < y2) ? 1 : -1;
    int err = dx - dy;
    while (1)
    {
        putpixel(x1, y1, BLACK);
        if (x1 == x2 && y1 == y2)
            break;
        int e2 = err * 2;
        if (e2 > -dy)
        {
            err -= dy;
            x1 += sx;
        }
        if (e2 < dx)
        {
            err += dx;
            y1 += sy;
        }
    }
}
void drawStar(int cx, int cy, int radius)
{
    double angle = 2 * M_PI / 5;
    int x[5], y[5];
    for (int i = 0; i < 5; i++)
    {
        x[i] = cx + radius * cos(i * angle);
        y[i] = cy - radius * sin(i * angle);
    }
    for (int i = 0; i < 5; i++)
    {
        bresenhamLine(x[i], y[i], x[(i + 2) % 5], y[(i + 2) % 5]);
    }
}
int main()
{
    int gd = DETECT, gm;
    initgraph(&gd, &gm, "");
    setbkcolor(WHITE);
    cleardevice();
    drawStar(300, 250, 100);
    getch();
    closegraph();
    return 0;
}