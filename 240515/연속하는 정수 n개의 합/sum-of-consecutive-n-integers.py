n,target = map(int,input().split())
arr=list(map(int,input().split()))


total, j, cnt = 0, 0, 0
for i in range(n):
    # 구간합이 m보다 작으면 계속 진행
    while j < n and total < target :
        total += arr[j]
        j += 1

    if total == target :
        cnt += 1
    
    total -= arr[i]

print(cnt)