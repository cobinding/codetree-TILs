line = [0 for _ in range(2001)]

n = int(input())
recent = 1000

for _ in range(n):
    x, direction = input().split()
    x = int(x)
 
    if direction == "L":
        for i in range(recent-1, recent-x-1, -1):
            line[i] += 1
        recent -= x

    elif direction == "R":
        for i in range(recent, recent+x):
            line[i] += 1
        recent += x

cnt = 0
for item in line:
    if item >= 2: 
        cnt += 1

"""for i in range(6, 1, -1): # 5, 4, 3, 2
    print(i)"""

print(cnt)