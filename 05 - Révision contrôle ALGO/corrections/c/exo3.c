#include <stdio.h>

int incompatible[20][20];
int chosen[20];
int n;
int best;
int count;

void search(int member, int size) {
    if (member == n) {
        if (size > best) {
            best = size;
            count = 1;
        } else if (size == best) {
            count++;
        }
        return;
    }

    search(member + 1, size);

    for (int previous = 0; previous < member; previous++) {
        if (chosen[previous] && incompatible[previous][member]) {
            return;
        }
    }
    chosen[member] = 1;
    search(member + 1, size + 1);
    chosen[member] = 0;
}

int main(void) {
    int m;
    scanf("%d %d", &n, &m);

    for (int i = 0; i < m; i++) {
        int a, b;
        scanf("%d %d", &a, &b);
        incompatible[a - 1][b - 1] = 1;
        incompatible[b - 1][a - 1] = 1;
    }

    search(0, 0);
    printf("%d %d\n", best, count);
    return 0;
}
