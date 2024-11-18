#include <graphics.h>

// Function for 8-connected boundary fill
void boundaryFill8(int x, int y, int fill_color, int boundary_color) {
    if (getpixel(x, y) != boundary_color && getpixel(x, y) != fill_color) {
        putpixel(x, y, fill_color);

        boundaryFill8(x + 1, y,     fill_color, boundary_color); // Right
        boundaryFill8(x - 1, y,     fill_color, boundary_color); // Left
        boundaryFill8(x,     y + 1, fill_color, boundary_color); // Down
        boundaryFill8(x,     y - 1, fill_color, boundary_color); // Up
        boundaryFill8(x + 1, y + 1, fill_color, boundary_color); // Diagonal (Down-Right)
        boundaryFill8(x - 1, y + 1, fill_color, boundary_color); // Diagonal (Down-Left)
        boundaryFill8(x + 1, y - 1, fill_color, boundary_color); // Diagonal (Up-Right)
        boundaryFill8(x - 1, y - 1, fill_color, boundary_color); // Diagonal (Up-Left)
    }
}

int main() {
    int gd = DETECT, gm;
    initgraph(&gd, &gm, ""); // Initialize graphics

    // Example: Fill a rectangle
    rectangle(50, 50, 100, 100); // Draw a rectangle (boundary)
    boundaryFill8(55, 55, 4, 15); // Fill with color 4, boundary color 15

    delay(100000); //Pause for visualization
    getch();
    closegraph();
    return 0;
}