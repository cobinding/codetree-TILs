from collections import deque

# ----- 실패 코드 메모용 ----- # 

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
cnt = 0
d = [(1,0), (0,1), (-1,0), (0,-1)]
visited = [[False]*(n) for _ in range(n)]
cost = 0

def searchQue(x, y) :
    visited[x][y] = True
    q = deque()
    q.append((x, y))
    tmp = 0
    
    while q :
        x, y = q.popleft()
        
        for dx, dy in d:
            nx, ny = x+dx, y+dy
                
            # 현재 위치에서 k만큼 상하좌우를 탐색했을 때 n보다 크면 안됨
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] == 1 and not visited[nx][ny]: 
                    tmp += 1
                    q.append((nx, ny))
                    visited[nx][ny] = True
                else:
                    break
    
    return tmp

for i in range(n):
    for j in range(n):
        visited[i][j] = True
        cnt += searchQue(i, j)
        
print(cnt)