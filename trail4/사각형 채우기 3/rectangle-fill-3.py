n = int(input())

dp = [0] * max(4, n + 1)

dp[0] = 1 
dp[1] = 2
dp[2] = 7

for i in range(3, n + 1):
    dp[i] = dp[i-1] * 3 + dp[i-2] * 1 - dp[i-3] * 1

print(dp[n]%1000000007)

