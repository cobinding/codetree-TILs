n,m=map(int,input().split())
arr=list(map(int,input().split()))

for _ in range(m):
    val=int(input())

    left,right=0,n-1
    while left<=right:
        mid=(left+right)//2

        if val < arr[mid]:
            right=mid-1
        elif val > arr[mid]:
            left=mid+1
        else:
            break
    
    if val in arr:
        print(mid+1)
    else:
        print(-1)