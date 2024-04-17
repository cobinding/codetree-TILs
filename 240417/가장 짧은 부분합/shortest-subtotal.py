import sys;input=sys.stdin.readline

n,s=map(int,input().split())
arr=[0] + list(map(int,input().split()))

# 합이 s 이상인 것 중에 구간이 가장 짧아야 함.


INT_MAX=sys.maxsize
ans=INT_MAX

for i in range(1,n+1):
    # i가 시작점, 시작점마다 total 초기화!
    
    total=0
    for j in range(i,n+1):
        total += arr[j]
        
        if total >= s: 
            ans=min(ans,j-i+1)
            total -= arr[i]

if ans == INT_MAX: ans=-1

print(ans)