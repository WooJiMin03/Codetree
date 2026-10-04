N, M = map(int, input().split())
w, v = zip(*[tuple(map(int, input().split())) for _ in range(N)])
w, v = list(w), list(v)
dp=[[0]*(M+1) for _ in range(N+1)]

for i in range(1,N+1):
    for j in range(1,M+1):
        if(j<w[i-1]):
            dp[i][j]=dp[i-1][j]
        elif(j>=w[i-1]):
            dp[i][j]=max(dp[i-1][j],dp[i][j-w[i-1]]+v[i-1])

best=0
for i in range(N+1):
    for j in range(M+1):
        best=max(best,dp[i][j])

print(best)

# Please write your code here.
