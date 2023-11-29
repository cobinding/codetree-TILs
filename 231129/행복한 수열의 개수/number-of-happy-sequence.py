n,m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
cnt = 0

# 행 체크
for row in graph:
    row_cnt = 1
    for i in range(n-1):
        if row[i] == row[i+1]:
            row_cnt += 1
        else: 
            row_cnt = 1

        # 하나의 행에 동일한 값이 m개라면
        if row_cnt == m: 
            cnt += 1
            break
    
        
# 열 체크
for i in range(n):
    col_cnt = 1
    for j in range(n-1):
        if graph[j][i] == graph[j+1][i]:
            col_cnt += 1
        else: 
            col_cnt = 1
        
        # 하나의 열에 동일한 값이 m개라면
        if col_cnt == m :
            cnt += 1
            break

if n == 1 :
    print(n*2)
else:
    print(cnt)