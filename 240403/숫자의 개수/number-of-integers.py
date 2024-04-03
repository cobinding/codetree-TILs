n,m=map(int,input().split())
arr=list(map(int,input().split()))

for _ in range(m):
    target=int(input())
    left,right=0,n-1
    
    lower_idx,upper_idx=n,n

    # lower bound
    while left<=right:
        mid=(left+right)//2
        if target<=arr[mid]:
            lower_idx=min(lower_idx,mid)
            right=mid-1
        else:
            left=mid+1
    
    left,right=0,n-1
    # upper bound
    while left<=right:
        mid=(left+right)//2
        if target<arr[mid]:
            upper_idx=min(upper_idx,mid)
            right=mid-1
        else:
            left=mid+1

        
    print(upper_idx-lower_idx)