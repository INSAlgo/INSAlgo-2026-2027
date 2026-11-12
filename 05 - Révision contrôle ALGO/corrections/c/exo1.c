#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int n;
    scanf("%d", &n);

    int *level = malloc(n * sizeof(int));
    for (int i = 0; i < n; i++) {
        scanf("%d", &level[i]);
    }

    int records = 1;
    int best = level[0];
    for (int i = 1; i < n; i++) {
        if (level[i] > best) {
            records++;
            best = level[i];
        }
    }

    int max_variation = 0;
    for (int i = 1; i < n; i++) {
        int variation = abs(level[i] - level[i - 1]);
        if (variation > max_variation) {
            max_variation = variation;
        }
    }

    int longest = 1;
    int current = 1;
    for (int i = 1; i < n; i++) {
        if (level[i - 1] <= level[i]) {
            current++;
        } else {
            current = 1;
        }
        if (current > longest) {
            longest = current;
        }
    }

    printf("%d %d %d\n", records, max_variation, longest);
    free(level);
    return 0;
}
