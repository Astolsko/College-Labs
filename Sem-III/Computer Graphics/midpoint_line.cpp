#include <iostream>
#include <graphics.h>

using namespace std;

// Midpoint Line Drawing Algorithm
void line_midpoint(int x0, int y0, int x1, int y1) {
    int dx = x1 - x0;
    int dy = y1 - y0;
    int d = 2 * dy - dx; // Initial decision parameter
    int y = y0;

    // Loop through the x coordinates
    for (int x = x0; x <= x1; x++) {
        putpixel(x, y, WHITE); // Plot the point

        // If the decision parameter d is greater than or equal to 0
        if (d >= 0) {
            y++; // Increment y coordinate
            d += 2 * (dy - dx); // Update decision parameter
        } else {
            d += 2 * dy; // Update decision parameter
        }
    }
}


int main(){

    
    int gdriver=DETECT, gmode;  
    initgraph(&gdriver, &gmode, (char*)"");  

    line_midpoint(100, 100, 250, 250);
    getch();
    closegraph();

    return 0;
}