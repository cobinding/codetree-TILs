n, k = map(int,input().split())
arr = [0 for _ in range(n)]

for _ in range(k):
    start, end = map(int,input().split())
    for i in range(start-1, end):
        arr[i] += 1

print(max(arr))