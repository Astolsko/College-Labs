#include <graphics.h>
#include <math.h>
#include <stdio.h>

// Function for finding absolute value
int abs_val(int n) { return ((n > 0) ? n : (n * (-1))); }

void boundary_fill(int x, int y, int fill_color, int boundary_color) {
    int current_color = getpixel(x, y);
    if (current_color != boundary_color && current_color != BLUE && current_color != fill_color) {
        putpixel(x, y, fill_color);
        boundary_fill(x + 1, y, fill_color, boundary_color);
        boundary_fill(x - 1, y, fill_color, boundary_color);
        boundary_fill(x, y + 1, fill_color, boundary_color);
        boundary_fill(x, y - 1, fill_color, boundary_color);
    }
}

// DDA Function for line generation
void DDA(int X0, int Y0, int X1, int Y1) {
    // calculate dx & dy
    int dx = X1 - X0;
    int dy = Y1 - Y0;
    // calculate steps required for generating pixels
    int steps = abs_val(dx) > abs_val(dy) ? abs_val(dx) : abs_val(dy);
    // calculate increment in x & y for each step
    float Xinc = dx / (float)steps;
    float Yinc = dy / (float)steps;
    // Put pixel for each step
    float X = X0;
    float Y = Y0;
    for (int i = 0; i <= steps; i++) {
        putpixel(round(X), round(Y), BLACK); // Change to BLACK color for the pixel
        X += Xinc; // increment in x at each step
        Y += Yinc; // increment in y at each step
        // delay(10); // Optional: Remove or adjust delay for faster drawing
    }
}

void plot_circle_points(int xc, int yc, int x, int y) {
    putpixel(xc + x, yc + y, BLUE); // Octant 1
    putpixel(xc - x, yc + y, BLUE); // Octant 2
    putpixel(xc + x, yc - y, BLUE); // Octant 3
    putpixel(xc - x, yc - y, BLUE); // Octant 4
    putpixel(xc + y, yc + x, BLUE); // Octant 5
    putpixel(xc - y, yc + x, BLUE); // Octant 6
    putpixel(xc + y, yc - x, BLUE); // Octant 7
    putpixel(xc - y, yc - x, BLUE); // Octant 8
}

// Mid-point Circle Drawing Algorithm
void draw_circle(int xc, int yc, int r) {
    int x = 0, y = r;
    int p = 1 - r; // Initial decision parameter
    // Plot the initial points
    plot_circle_points(xc, yc, x, y);
    // Use the midpoint algorithm to plot the points
    while (x < y) {
        x++; // Move to the next point along x-axis
        if (p < 0) {
            p = p + 2 * x + 1; // Midpoint is inside or on the perimeter
        } else {
            y--; // Midpoint is outside the circle
            p = p + 2 * x - 2 * y + 1;
        }
        // Plot the points in all 8 octants
        plot_circle_points(xc, yc, x, y);
    }
}

// Function to draw a rectangle using DDA
void draw_rectangle(int x1, int y1, int x2, int y2) {
    // Draw the four sides of the rectangle
    DDA(x1, y1, x2, y1); // Top horizontal line
    DDA(x2, y1, x2, y2); // Right vertical line
    DDA(x2, y2, x1, y2); // Bottom horizontal line
    DDA(x1, y2, x1, y1); // Left vertical line
}

void divide_rectangle(int x1, int y1, int x2, int y2) {
    // Calculate the width of each part
    int part_width = (y2 - y1) / 3;
    // Draw horizontal lines to divide the rectangle into 3 parts
    DDA(x1, y1 + part_width, x2, y1 + part_width); // 1st dividing line
    DDA(x1, y1 + 2 * part_width, x2, y1 + 2 * part_width); // 2nd dividing line
    // Calculate center and radius for the circle
    int xc = (x1 + x2) / 2;
    int yc = (y1 + y2) / 2;
    int r = part_width / 2;
    // Draw the circle
    draw_circle(xc, yc, r);
    // Draw 24 spokes inside the circle
    int num_spokes = 24;
    for (int i = 0; i < num_spokes; i++) {
        // Calculate angle in degrees
        float angle_deg = i * (360.0 / num_spokes);
        // Convert angle to radians
        float angle_rad = angle_deg * (M_PI / 180.0);
        // Calculate end point of the spoke
        int x_end = round(xc + r * cos(angle_rad));
        int y_end = round(yc + r * sin(angle_rad));
        // Draw the spoke from center to end point
        DDA(xc, yc, x_end, y_end);
    }
}

int main() {
    int gd = DETECT, gm;
    initgraph(&gd, &gm, "");
    setbkcolor(WHITE);
    cleardevice(); // Clear the device with the new background color
    // Coordinates for drawing the larger rectangle
    int x1 = 100, y1 = 100; // Top-left corner
    int x2 = 500, y2 = 300; // Bottom-right corner
    // Draw the larger rectangle using DDA
    draw_rectangle(x1, y1, x2, y2);
    // Divide the rectangle into 3 parts along the breadth and add circle with spokes
    divide_rectangle(x1, y1, x2, y2);
    int up = 14;
    boundary_fill(205, 150, YELLOW, BLACK);
    boundary_fill(205, 280, GREEN, BLACK);
    getch();
    closegraph();
    return 0;
}