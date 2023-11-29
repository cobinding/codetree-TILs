n,m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
cnt = 0

# 행 체크
for row in graph:
    row_cnt = 1
    for i in range(1, n):
        if row[i] == row[i-1]: row_cnt += 1

    # 하나의 행에 동일한 값이 m개라면
    if row_cnt >= m: cnt += 1
    
        
# 열 체크
for i in range(n):
    col_cnt = 1
    for j in range(1, n):
        if graph[j-1][i] == graph[j][i]: col_cnt += 1
        
    # 하나의 열에 동일한 값이 m개라면
    if col_cnt >= m : cnt += 1

print(cnt)