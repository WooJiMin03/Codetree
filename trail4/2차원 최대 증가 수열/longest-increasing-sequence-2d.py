n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1]*m for _ in range(n)]
dp[0][0]=1

for i in range(1,n):
    for j in range(1,m): # 선택 끝
        for q in range(i):
            for w in range(j):
                if(dp[q][w]==-1 or grid[i][j]<=grid[q][w]):
                    continue

                dp[i][j]=max(dp[i][j],dp[q][w]+1)
best = 0
for row in dp:
    best = max(best, max(row))
print(best)
# Please write your code here.
