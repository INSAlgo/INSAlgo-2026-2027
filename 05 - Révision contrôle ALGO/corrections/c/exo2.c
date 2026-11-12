#include <stdio.h>

int main(void) {
    long long u[64];
    int m = 2;
    u[0] = 1;
    u[1] = 4;
    const long long limit = 1000000000000000000;
    while (1) {
        long long next = 2 * u[m - 1] + u[m - 2] + 1;
        if (next > limit) {
            break;
        }
        u[m] = next;
        m++;
    }

    int t;
    scanf("%d", &t);
    for (int query = 0; query < t; query++) {
        long long n;
        scanf("%lld", &n);

        int k = -1;
        for (int i = 0; i < m; i++) {
            if (u[i] == n) {
                k = i + 1;
                break;
            }
        }
        printf("%d\n", k);
    }
    return 0;
}
