#include <iostream>
#include <graphics.h>
#include <conio.h>

void draw_circle_points(int xc, int yc, int x, int y) {
    putpixel(xc + x, yc + y, WHITE);
    putpixel(xc - x, yc + y, WHITE);
    putpixel(xc + x, yc - y, WHITE);
    putpixel(xc - x, yc - y, WHITE);
    putpixel(xc + y, yc + x, WHITE);
    putpixel(xc - y, yc + x, WHITE);    
    putpixel(xc + y, yc - x, WHITE);
    putpixel(xc - y, yc - x, WHITE);
}

void midpoint_circle(int xc, int yc, int r) {
    int x = 0, y = r;
    int d = 1 - r;  // Decision parameter

    draw_circle_points(xc, yc, x, y);  // Initial points

    while (x < y) {
        x++;
        if (d < 0) {
            d = d + 2 * x + 1;
        } else {
            y--;
            d = d + 2 * (x - y) + 1;
        }
        draw_circle_points(xc, yc, x, y);
    }
}

void drawline(int x0, int y0, int x1, int y1) {
    int dx = abs(x1 - x0);
    int dy = abs(y1 - y0);
    int sx = (x0 < x1) ? 1 : -1;  // Step in the x direction
    int sy = (y0 < y1) ? 1 : -1;  // Step in the y direction
    int err = dx - dy;

    while (true) {
        putpixel(x0, y0, WHITE);  // Draw the pixel
        if (x0 == x1 && y0 == y1) break;  // Stop if the end point is reached

        int e2 = 2 * err;
        if (e2 > -dy) {  // Adjust x based on decision parameter
            err -= dy;
            x0 += sx;
        }
        if (e2 < dx) {  // Adjust y based on decision parameter
            err += dx;
            y0 += sy;
        }
    }
}


void fill_circle(int xc, int yc, int r, int color) {
    setcolor(color);
    setfillstyle(SOLID_FILL, color);
    fillellipse(xc, yc, r, r);  // Fill the circle with color
}

void clear_circle(int xc, int yc, int r) {
    setcolor(BLACK);
    setfillstyle(SOLID_FILL, BLACK);
    fillellipse(xc, yc, r, r);  // Clear the circle (fill with black)
}


int main(){

    int gd = DETECT, gm;
    initgraph(&gd, &gm, (char*)"");

    // Draw the traffic light structure (rectangle)
    int x1 = 200, y1 = 100, x2 = 250, y2 = 300;
    drawline(x1, y1, x1, y2);
    drawline(x1, y1, x2, y1);
    drawline(x1, y2, x2, y2);
    drawline(x2, y1, x2, y2);
    
    int r = 18;
    int xc0 = 225, yc0 = 150;  // Red light
    int xc1 = 225, yc1 = 200;  // Yellow light
    int xc2 = 225, yc2 = 250; 
    midpoint_circle(xc0, yc0, r);
    
    midpoint_circle(xc1, yc1, r);
    
    midpoint_circle(xc2, yc2, r);
    
    while (true) {
        // Turn on red light
        clear_circle(xc2, yc2, r);
        fill_circle(xc0, yc0, r, RED);
        // clear_circle(xc1, yc1, r);  // Clear yellow light
          // Clear green light
        delay(1000);

        // Turn on yellow light
        fill_circle(xc1, yc1, r, YELLOW);
        clear_circle(xc0, yc0, r);  // Clear red light
        // clear_circle(xc2, yc2, r);  // Clear green light
        delay(1000);

        // Turn on green light
        fill_circle(xc2, yc2, r, GREEN);
        clear_circle(xc0, yc0, r);  // Clear red light
        clear_circle(xc1, yc1, r);  // Clear yellow light
        delay(1000);
    }


    getch();
    closegraph();
    return 0;

}