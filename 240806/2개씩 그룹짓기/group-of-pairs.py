n = int(input())
arr = sorted(map(int, input().split()))

group_max = 0
for i in range(n):
    # 양 끝쪽에서부터 덧셈하기
    max_sum = arr[i] + arr[n*2-i-1]
    if max_sum > group_max:
        group_max = max_sum
    
print(group_max)