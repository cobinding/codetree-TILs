n = int(input())
dp = [0 for _ in range(n+2)]
dp_half = [0 for _ in range(n+2)]

dp[1] = 2
dp[2] = 7
dp_half[1] = 1
dp_half[2] = 3


for i in range(3, n+1):
    # half 두개 세로로 겹치는 경우는 dp에서 측정
    dp[i] = dp[i-1]*2 + dp[i-2] + dp_half[i-1]*2
    dp_half[i] = dp[i-1] + dp_half[i-1]

print(dp[n]%1000000007)