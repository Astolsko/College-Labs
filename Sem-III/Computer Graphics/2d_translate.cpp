#include <graphics.h>
#include <iostream>
using namespace std;

int main()
{
    int gd = DETECT, gm;

    initgraph(&gd, &gm, " ");
    int xi = 250, yi = 200, r = 100;
    circle(xi, yi, r);
    // Translation;
    int tx = 100;
    int ty = 150;
    circle(xi + tx, yi + ty, r);

    getch();
    closegraph();
    return 0;
}