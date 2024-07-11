n,m=map(int,input().split())

def get_lcm(n,m):
    lcm=0
    # 최소공배수는 두 수의 곱보다 작을 수 없음
    for i in range(max(n,m), n*m+1):
        # 현재 값이 n과 m의 공통 배수인지 확인
        if i%n==0 and i%m==0:
            lcm=i
            break
    
    return lcm

print(get_lcm(n,m))