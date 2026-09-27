n = int(input())
jobs = [tuple(map(int, input().split())) for _ in range(n)]
s = [job[0] for job in jobs]
e = [job[1] for job in jobs]
p = [job[2] for job in jobs]
dp=[0]*n

for i in range(n):
    dp[i] = p[i]

for i in range(n):
    for j in range(0,i):
        if(e[j]<s[i]):
            dp[i]=max(dp[i],dp[j]+p[i])
print(max(dp))
# Please write your code here.
