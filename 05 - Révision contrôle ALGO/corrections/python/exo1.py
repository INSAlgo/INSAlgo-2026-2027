n = int(input())
level = list(map(int, input().split()))

records = 1
best = level[0]
for i in range(1, n):
    if level[i] > best:
        records += 1
        best = level[i]

max_variation = 0
for i in range(1, n):
    variation = abs(level[i] - level[i - 1])
    if variation > max_variation:
        max_variation = variation

longest = 1
current = 1
for i in range(1, n):
    if level[i - 1] <= level[i]:
        current += 1
    else:
        current = 1
    if current > longest:
        longest = current

print(records, max_variation, longest)
