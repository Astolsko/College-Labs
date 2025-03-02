#include <graphics.h>

void boundaryFill4(int x, int y, int fill_color, int boundary_color)
{
    if (getpixel(x, y) != boundary_color && getpixel(x, y) != fill_color)
    {
        putpixel(x, y, fill_color);
        boundaryFill4(x + 1, y, fill_color, boundary_color);
        boundaryFill4(x, y + 1, fill_color, boundary_color);
        boundaryFill4(x - 1, y, fill_color, boundary_color);
        boundaryFill4(x, y - 1, fill_color, boundary_color);
    }
}
int main()
{
    int gd = DETECT, gm;
    initgraph(&gd, &gm, "");
    setbkcolor(WHITE);
    cleardevice();
    int x = 250, y = 200, radius = 50;
    setcolor(BLACK);
    circle(x, y, radius);
    boundaryFill4(x, y, 6, BLACK);
    delay(10);
    getch();
    closegraph();
    return 0;
}