#include <iostream>
#include <graphics.h>
#include <cmath>

// Bresenham's line algorithm (same as before)
void bresenham_line(int x1, int y1, int x2, int y2)
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
// Function to draw a circle using Bresenham's circle algorithm (optional; midpoint is simpler)
void bresenhamCircle(int xc, int yc, int r) {
    int x = 0;
    int y = r;
    int d = 3 - 2 * r;
    while (y >= x) {
        putpixel(xc + x, yc + y, WHITE);
        putpixel(xc - x, yc + y, WHITE);
        putpixel(xc + x, yc - y, WHITE);
        putpixel(xc - x, yc - y, WHITE);
        putpixel(xc + y, yc + x, WHITE);
        putpixel(xc - y, yc + x, WHITE);
        putpixel(xc + y, yc - x, WHITE);
        putpixel(xc - y, yc - x, WHITE);
        x++;
        if (d > 0) {
            y--;
            d = d + 4 * (x - y) + 10;
        } else {
            d = d + 4 * x + 6;
        }
    }
}
// Function to draw a hut
void draw_hut(int base_x, int base_y, int width, int height) {
    // Draw the rectangular base of the hut
    bresenham_line(base_x, base_y, base_x + width, base_y);           // Top
    bresenham_line(base_x, base_y + height, base_x + width, base_y + height); // Bottom
    bresenham_line(base_x, base_y, base_x, base_y + height);          // Left side
    bresenham_line(base_x + width, base_y, base_x + width, base_y + height); // Right side

    // Draw the triangular roof
    int roof_height = height / 2; // Adjust roof height as needed
    int roof_peak_x = base_x + width / 2;
    int roof_peak_y = base_y - roof_height;

    bresenham_line(base_x, base_y, roof_peak_x, roof_peak_y); // Left side of roof
    bresenham_line(base_x + width, base_y, roof_peak_x, roof_peak_y); // Right side of roof

    // Draw the inner rectangle
    int inner_rect_width = width / 2; // Width of the inner rectangle
    int inner_rect_height = height / 3; // Height of the inner rectangle
    int inner_rect_x = base_x + (width - inner_rect_width) / 2; // Centering it horizontally
    int inner_rect_y = base_y + (2 * height) / 3; // Position it in the lower part of the hut

    bresenham_line(inner_rect_x, inner_rect_y, inner_rect_x + inner_rect_width, inner_rect_y); // Top
    bresenham_line(inner_rect_x, inner_rect_y + inner_rect_height, inner_rect_x + inner_rect_width, inner_rect_y + inner_rect_height); // Bottom
    bresenham_line(inner_rect_x, inner_rect_y, inner_rect_x, inner_rect_y + inner_rect_height); // Left side
    bresenham_line(inner_rect_x + inner_rect_width, inner_rect_y, inner_rect_x + inner_rect_width, inner_rect_y + inner_rect_height); // Right side
}



int main() {
    int gd = DETECT, gm;
    initgraph(&gd, &gm, (char*)""); // Initialize graphics


    // Set background color
    setbkcolor(WHITE);
    cleardevice();


    // House dimensions
    int houseX = 100;
    int houseY = 100;
    int houseWidth = 150;
    int houseHeight = 120;
    int roofHeight = 50;
    int doorWidth = 40;
    int doorHeight = 60;
    int windowSize = 30; //Side of square window

    // Draw the house
    draw_hut(houseX, houseY, houseX + houseWidth, houseY + houseHeight); // House base

    getch();
    closegraph();
    return 0;
}