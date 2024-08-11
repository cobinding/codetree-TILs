n = int(input())

line = [0 for _ in range(200)]

for _ in range(n):
    x1, x2 = map(int, input().split())

    for i in range(x1, x2):
        line[i] += 1

print(max(line))