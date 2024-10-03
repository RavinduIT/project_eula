#include <stdio.h>
#include <stdlib.h>

long sum_of_multiples(int k, int N) {
    int m = (N - 1) / k;  // Maximum multiple of k below N
    return (long)k * m * (m + 1) / 2;  // Sum of multiples of k below N
}

int main() {
    int t;
    scanf("%d", &t);
    int *n = (int *)malloc(t * sizeof(int));

    for (int a0 = 0; a0 < t; a0++) {
        scanf("%d", &n[a0]);
    }

    for (int i = 0; i < t; i++) {
        int N = n[i];
        long sum = sum_of_multiples(3, N) + sum_of_multiples(5, N) - sum_of_multiples(15, N);
        printf("%ld\n", sum);
    }

    free(n);
    n = NULL;
    return 0;
}
