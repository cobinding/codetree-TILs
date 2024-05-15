import sys;input=sys.stdin.readline

n,k=map(int,input().split())
arr=[int(input()) for _ in range(n)]


arr.sort()

e=n-1
cnt=0

for s in range(n):
    while e != 1 and arr[s]+arr[e] > k:
        e -= 1
    
    if e <= s :
        break

    cnt += e-s

print(cnt)