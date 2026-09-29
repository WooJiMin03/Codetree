n = int(input())
dp=[-1]*(n+1)
for i in range(n+1):
    dp[i]=0
dp[0]=1
coin=[1,2,5]
for i in range(1,n+1):
    for j in range(3):
        if(i>=coin[j]):
            dp[i]+=dp[i-coin[j]]
print(dp[n]%10007)
# 1 , 2 , 3,
# Please write your code here.
