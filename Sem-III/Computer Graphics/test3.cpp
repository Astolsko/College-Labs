#include <graphics.h>
#include <conio.h>
#include <stdio.h>
#include <dos.h>
#include <stdlib.h>

int main() {
    int graphicdriver = DETECT, graphicmode;
    int num_bars, i;
    int min_range = 0;
    int max_range = 100;

    initgraph(&graphicdriver, &graphicmode, "c:\\turboc3\\bgi");

    printf("Enter the number of bars: ");
    scanf("%d", &num_bars);

    int heights[num_bars];

    for(i = 0; i < num_bars; i++) {
        printf("Enter height for bar %d: ", i + 1);
        scanf("%d", &heights[i]);
    }

    int min = heights[0];
    int max = heights[0];
    int size = num_bars;

    for(int i = 1; i < size; i++) {
        if(heights[i] < min) {
            min = heights[i];
        }
        if(heights[i] > max) {
            max = heights[i];
        }
    }

    int scaled_heights[num_bars];

    if(max > 100) {
        for(int i = 0; i < size; i++) {
            scaled_heights[i] = ((heights[i] - min) * (max_range - min_range)) / (max - min) + min_range;
        }
    } else {
        for(int j = 0; j < size; j++) {
            scaled_heights[j] = heights[j];
        }
    }

    int mini = scaled_heights[0];

    for(int i = 1; i < size; i++) {
        if(scaled_heights[i] < mini) {
            mini = scaled_heights[i];
        }
    }

    for(int i = 1; i < size; i++) {
        if(scaled_heights[i] == mini) {
            scaled_heights[i] += 5;
            printf("%d", scaled_heights[i]);
        }
    }

    line(100, 420, 100, 120);
    line(100, 420, 500, 420);

    int bar_width = 50;
    int gap = 25;
    int x_start = 150;

    int y_axis_start = 420;
    int y_interval = 30;

    for (int value = 0; value <= 100; value += 10) {
        int y_pos = y_axis_start - (value / 10 * y_interval);
        char label[10];
        sprintf(label, "%d", value);
        outtextxy(70, y_pos - textheight(label) / 2, label);
    }

    for (int i = 0; i < num_bars; i++) {

        int color = i % 4 + 1;
        setfillstyle(SOLID_FILL, color);

        bar(x_start, 420 - 3 * int(scaled_heights[i]), x_start + bar_width, 419);

        char label[10];
        sprintf(label, "Bar %d", i + 1);
        outtextxy(x_start + bar_width / 2 - textwidth(label) / 2, 425, label);

        x_start += bar_width + gap;
    }


    getch();
    closegraph();
    return 0;
}
