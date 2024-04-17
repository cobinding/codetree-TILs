### 중복되는 숫자가 없어야하고, 최대 구간 크기

n=int(input())
arr=[0] + list(map(int,input().split()))
cnt_arr=[0]*(max(arr)+1)

ans=0
j=0
for i in range(1,n+1):
    while j+1 <= n and cnt_arr[arr[j+1]] < 1:
        cnt_arr[arr[j+1]] += 1
        j += 1
    
    ans=max(ans,j-i+1)

print(ans+1)