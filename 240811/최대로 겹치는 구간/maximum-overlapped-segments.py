n = int(input())

line = [0 for _ in range(101)]

cnt = 0
for _ in range(n):
    x1, x2 = map(int, input().split())

    for i in range(x1, x2):
        line[i] += 1
        if line[i] >= 2 :
            cnt += 1
            break

print(cnt)