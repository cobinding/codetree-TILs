import sys;input=sys.stdin.readline

n=int(input())
arr=sorted(map(int,input().split()))

start,end=0,n-1
min_sum=sys.maxsize

while start < end and start <= 0:
     
    sum_numbers=arr[start]+arr[end]
    min_sum=min(abs(sum_numbers), min_sum)

    if sum_numbers > 0 :
        end -= 1
    elif sum_numbers < 0 :
        start += 1
    else: 
        print(0)
        exit(1)
    

print(abs(min_sum))