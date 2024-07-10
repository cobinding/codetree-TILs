# n: 행 반복, m: 별 개수
n,m=map(int,input().split())

# 1을 m번 반복하여 출력하는 함수
def print_one_m():
    print("1"*m)

# n번 반복하여 함수를 호출
for _ in range(n):
    print_one_m()