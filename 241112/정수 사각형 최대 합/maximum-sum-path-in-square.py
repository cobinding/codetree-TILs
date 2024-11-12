n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
# 오른쪽: (i, j+1) 밑: (i+1, j)

dp = [[0 for _ in range(n)] for _ in range(n)]
dp[0][0] = graph[0][0]

# 자신의 자리에서 dp table과 비교 및 저장
for i in range(n):
    for j in range(n):
        dp[i][j] = max(graph[i][j]+dp[i][j-1], graph[i][j]+dp[i-1][j])

print(dp[-1][-1])