n, m = map(int, input().split())
A = list(map(int, input().split()))

dp = [False] * (m + 1)
dp[0] = True 

for a in A:
    for i in range(m, a - 1, -1):
        if dp[i - a] == True:
            dp[i] = True

if(dp[m]):
    print("Yes")
else:
    print("No")
# Please write your code here.
