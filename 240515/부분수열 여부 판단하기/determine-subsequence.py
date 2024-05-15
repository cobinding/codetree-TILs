n,m=map(int,input().split())
A=[0] + list(map(int,input().split()))
B=[0] + list(map(int,input().split()))

def is_subsequence():
    i = 1

    # B의 원소를 기준으로 A[i]와 일치한지 검사
    for j in range(1, m+1):
        # A[i]와 B[j]가 일치하지 않다면 
        while i <= n and A[i] != B[j]:
            i += 1
        

        # 다 돌았는데 못찾으면 부분수열이 아님
        if i == n+1 :
            return False
        # 다 돌지않았고, while이 끝나면 A 수열도 한 칸 이동
        else:
            i += 1
    
    return True


if is_subsequence():
    print("Yes")
else:
    print("No")