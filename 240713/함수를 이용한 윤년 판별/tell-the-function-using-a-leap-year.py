y=int(input())

# 4로 나누어 떨어지는 해 중, 예외 케이스를 처리하는 함수
def solve(n):
    if n%100==0 and n%400!=0:
        return false
    return True
    
if y%4==0:
    if solve(y): print('true')
    else: print('false')
else:
    print('false')