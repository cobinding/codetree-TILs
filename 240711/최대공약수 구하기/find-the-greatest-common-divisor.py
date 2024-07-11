n,m=map(int,input().split())

ans=0
for i in range(min(n,m), 1, -1):
    if n%i == 0 and m%i == 0:
        ans=i
        break

print(ans)