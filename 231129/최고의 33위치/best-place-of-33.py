n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

li = []
for i in range(n-2):
    for j in range(n-2):
        
        total = 0
    
        for k in range(3):
            for l in range(3):
                total += graph[i+k][j+l]
        li.append(total)
        
print(max(li))