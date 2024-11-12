# 일단 최대로 가는 방향으로 이동

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
dp = [[0 for _ in range(n)] for _ in range(n)]

res = []
for i in range(n):
    for j in range(n):
        res.append(max(graph[i-1][j], graph[i][j-1]))

print(min(res))