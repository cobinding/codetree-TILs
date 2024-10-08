import sys; input=sys.stdin.readline

n = int(input())
visited = [False] * (n+1)
answer = []

def permutations(curr_num):
    if curr_num == n+1 :
        print(*answer)
        return

    # 1부터 n까지 순열을 만드는 과정
    for i in range(1, n+1):

        if visited[i] :
            continue

        # 사용한 숫자에 대한 방문 처리
        visited[i] = True
        answer.append(i)

        # 순서 보장을 위해 1씩 늘려가면서 함수 호출
        permutations(curr_num+1)

        # 재귀함수가 return된 숫자에 대해서는 pop을 함으로써 배열의 끝 부분 제거
        answer.pop()
        visited[i] = False

permutations(1)