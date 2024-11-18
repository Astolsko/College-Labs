#include <graphics.h>
#include <conio.h> // For getch()

// Function to draw a line using the midpoint algorithm (replace with your implementation)
// Midpoint Line Drawing Algorithm
void midpoint_line(int x0, int y0, int x1, int y1) {
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


void draw_parallelogram(int x1, int y1, int x2, int y2, int height) {
    // Calculate the other two vertices of the parallelogram
    int x3 = x1 + (x2 - x1);
    int y3 = y1 + height;
    int x4 = x2 + (x2 - x1);
    int y4 = y2 + height;

    // Draw the four sides of the parallelogram
    midpoint_line(x1, y1, x2, y2);   // Top side
    midpoint_line(x3, y3, x4, y4);   // Bottom side
    midpoint_line(x1, y1, x3, y3);   // Left side
    midpoint_line(x2, y2, x4, y4);   // Right side
}

int main() {
    int gd = DETECT, gm;
    // Initialize graphics mode
    initgraph(&gd, &gm, "");

    // Define the coordinates for two vertices of the parallelogram
    int x1 = 200, y1 = 200; // First vertex
    int x2 = 400, y2 = 200; // Second vertex
    int height = 100;       // Height of the parallelogram

    draw_parallelogram(x1, y1, x2, y2, height);

    getch(); // Wait for a key press before closing the graphics window
    closegraph();
    return 0;
}