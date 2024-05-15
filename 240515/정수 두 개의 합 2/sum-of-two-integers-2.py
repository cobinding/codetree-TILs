n,k=map(int,input().split())

arr=[int(input()) for _ in range(n)]

cnt=0
for i in range(n):
    j=i+1

    while j<n:
        total = (arr[i]+arr[j])
        if total<=k:
            cnt+=1
        j+=1
    
print(cnt)