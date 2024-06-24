n,s=map(int,input().split())
arr=list(map(int,input().split()))

left,right=0,0
target=0
ans=float('inf') # 원소 값의 최대는 10,000

while True:
    target+=arr[right]

    while target>=s:
        ans=min(right-left+1, ans)
        
        # left pointer 조작을 통해 구간합 탐색
        target-=arr[left]
        left+=1

    # 끝까지 모두 탐색한 경우
    if right == n-1:
        break
    
    right += 1

print(ans)