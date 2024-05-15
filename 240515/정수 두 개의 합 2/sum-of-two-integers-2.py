import sys;input=sys.stdin.readline

n,k=map(int,input().split())
arr=[int(input()) for _ in range(n)]


arr.sort()

cnt=0
s,e=0,n-1

for s in range(n+1):
    if e != 1 and arr[s]+arr[e] > k:
        e -= 1

    if e <= s :
        break

    cnt += 1

print(cnt)