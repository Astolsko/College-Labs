#include <iostream>
#include <graphics.h>

using namespace std;

void plot(int x, int y) {
    int xc = 250, yc = 250;  // Center coordinates (adjust as needed)
    delay(1);
    putpixel(xc + x, yc + y, WHITE);
    delay(1);
    putpixel(xc - x, yc + y, WHITE);
    delay(1);
    putpixel(xc + x, yc - y, WHITE);
    delay(1);
    putpixel(xc - x, yc - y, WHITE);
}

void ellipse_midpoint(int rad_x, int rad_y){

    
    int x = 0;
    int y = rad_y;

    float p1 = rad_y * rad_y + 0.25*(rad_x * rad_x) - (rad_x * rad_x * rad_y);
    int dx = 2*rad_y*rad_y*x;
    int dy = 2*rad_x*rad_x*y;

    // first we plot for the region where slop is less than -1 .
    while(dx < dy){
        plot (x,y);
        if (p1 < 0){
            x++; // we keep on incrementing x
            dx = dx + 2*rad_y*rad_y; // after incrementing calculate the new dx
            p1 = p1 + dx + rad_y* rad_y;
            
        } // based on the parameter we keep y same or increment,
        else{
            x ++;
            y --;
            dx = dx + 2*rad_y*rad_y;
            dy = dy - 2 * rad_x * rad_x;
            p1 = p1 + dx - dy + rad_y * rad_y;
        }
    }

    float p2 = rad_y * rad_y * (x + 0.5)*(x + 0.5) + rad_x* rad_x*(y-1)*(y-1) - rad_x * rad_x * rad_y * rad_y;
    while (y > 0){
        plot (x,y);

        if(p2 >0){
            y--;
            dy = dy - 2*rad_x*rad_x;
            p2 = p2 - dy + rad_x*rad_x;
        }
        else{
            x++;
            y = y - 1;
            dy = dy - 2 * rad_x * rad_x;
            dx = dx + 2 * rad_y * rad_y;
            p2 = p2 + dx -dy + rad_x*rad_x;
        }

    }

}


int main(){

    int gdriver=DETECT, gmode;  
    initgraph(&gdriver, &gmode, (char*)"");  

    ellipse_midpoint(250, 130);
    getch();
    closegraph();


    return 0;
}