n, m = map(int, input().split())
incompatible = [[False] * n for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    incompatible[a - 1][b - 1] = True
    incompatible[b - 1][a - 1] = True

chosen = [False] * n
best = 0
count = 0


def search(member, size):
    global best, count
    if member == n:
        if size > best:
            best = size
            count = 1
        elif size == best:
            count += 1
        return

    search(member + 1, size)

    for previous in range(member):
        if chosen[previous] and incompatible[previous][member]:
            return
    chosen[member] = True
    search(member + 1, size + 1)
    chosen[member] = False


search(0, 0)
print(best, count)
