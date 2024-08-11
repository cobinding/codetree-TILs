line = [0 for _ in range(2001)]

n = int(input())
recent = 1000
for _ in range(n):
    x, direction = input().split()
 
    if direction == "L":
        for i in range(recent, recent-int(x)+1, -1):
            line[i] += 1
    elif direction == "R":
        for i in range(recent, recent+int(x)):
            line[i] += 1

cnt = 0
for item in line:
    if item >= 2: 
        cnt += 1

print(cnt)