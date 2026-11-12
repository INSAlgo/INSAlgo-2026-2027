u = [1, 4]
limit = 1000000000000000000
while True:
    next_value = 2 * u[-1] + u[-2] + 1
    if next_value > limit:
        break
    u.append(next_value)

t = int(input())
for _ in range(t):
    n = int(input())
    k = -1
    for i in range(len(u)):
        if u[i] == n:
            k = i + 1
            break
    print(k)
