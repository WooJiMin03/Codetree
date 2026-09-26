n = int(input())
arr = list(map(int, input().split()))
dp = [-float('inf')]*n
dp[0]=0
for i in range(1,n):
    for j in range(0,i):
        if(dp[j]==-float('inf')):
            continue
        if(j+arr[j]>=i):
            dp[i]=max(dp[i],dp[j]+1)

best=0
for i in range(n):
    if(best<dp[i]):
        best=dp[i]
print(best)
# Please write your code here.
