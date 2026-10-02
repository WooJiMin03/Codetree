n = int(input())
profit = list(map(int, input().split()))
dp = [0]*(n+1)
dp[0]=0
for i in range(1,n+1):
    for j in range(1,i+1):
        dp[i]=max(dp[i],dp[i-j]+profit[j-1])

print(dp[n])
# Please write your code here.
