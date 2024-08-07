n = int(input())
arr = list(map(int, input().split()))

for i in range(n):
    # 홀수 번째 수 == 인덱스가 짝수인 것
    if i == 0:
        print(arr[i], end = " ")
    elif i % 2 == 0:
        set_arr = sorted(arr[:i+1])
        print(set_arr[i//2], end = " ")