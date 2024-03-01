from collections import deque

n,k=map(int, input().split())
q=deque(range(1,n+1))

ans=[]
while len(q) != 0:
    for _ in range(k-1):
        tmp=q.popleft()
        q.append(tmp)
    ans.append(q.popleft())

print(*ans)