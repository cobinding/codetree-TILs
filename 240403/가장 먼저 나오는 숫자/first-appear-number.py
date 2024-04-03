n,m=map(int,input().split())
arr=list(map(int,input().split()))
search=list(map(int,input().split()))

for target in search:
    lower_idx=n
    left,right=0,n-1
    while left<=right:
        mid=(left+right)//2
        if target<=arr[mid]:
            lower_idx=min(lower_idx,mid)
            right=mid-1
        else:
            left=mid+1


    if lower_idx+1 <= n and arr[lower_idx] == target:
        print(lower_idx+1)
    else:
        print(-1)