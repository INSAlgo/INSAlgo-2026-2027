import sys
from collections import deque


def main():
    data = sys.stdin.read().split()
    n, k = int(data[0]), int(data[1])
    c = [0] + [int(x) for x in data[2 : 2 + n]]

    INF = float("inf")
    dp = [INF] * (n + 1)
    dp[0] = 0

    dq = deque([0])
    for i in range(1, n + 1):
        while dq and dq[0] < i - k:
            dq.popleft()
        dp[i] = c[i] + dp[dq[0]]
        while dq and dp[dq[-1]] >= dp[i]:
            dq.pop()
        dq.append(i)

    print(min(dp[n - k + 1 : n + 1]))


main()
