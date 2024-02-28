#include <stdio.h>
#include <math.h>
#include <stdlib.h>

// Define the range of values for n
#define N_VALUES 10

int main() {
    int n[N_VALUES];
    float x_n[N_VALUES];
    int i;

    // Generate values for n and x(n)
    for (i = 0; i < N_VALUES; i++) {
        n[i] = i;
        x_n[i] = 8 - 2 * n[i];
    }

    // Print the values of n and x(n)
    printf("n\t x(n)\n");
    for (i = 0; i < N_VALUES; i++) {
        printf("%d\t %.2f\n", n[i], x_n[i]);
    }

    return 0;
}

