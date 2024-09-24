#include <graphics.h>
#include <stdio.h>
#include <math.h>

void DDA(int x1, int y1, int x2, int y2) {
    int dx = x2 - x1;
    int dy = y2 - y1;

    int steps = abs(dx) > abs(dy) ? abs(dx) : abs(dy);

    float xIncrement = dx / (float) steps;
    float yIncrement = dy / (float) steps;

    float x = x1;
    float y = y1;

    putpixel(round(x), round(y), WHITE);

    for (int i = 0; i < steps; i++) {
        x += xIncrement;
        y += yIncrement;
        putpixel(round(x), round(y), WHITE);
    }
}

int main() {
    int gd = DETECT, gm;

    initgraph(&gd, &gm, "");
    int x1 = 100, y1 = 100;
    int x2 = 200, y2 = 100;
    int x3 = 150, y3 = 200;

    // Draw the triangle by connecting the vertices
    DDA(x1, y1, x2, y2);  // Line between (x1, y1) and (x2, y2)
    DDA(x2, y2, x3, y3);  // Line between (x2, y2) and (x3, y3)
    DDA(x3, y3, x1, y1);  // Line between (x3, y3) and (x1, y1)

    getch();
    closegraph();

    return 0;
}
