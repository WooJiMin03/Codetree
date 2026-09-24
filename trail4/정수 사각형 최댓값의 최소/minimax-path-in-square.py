n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        if((0<=i-1<n and 0<=j<n) and (0<=i<n and 0<=j-1<n)):
            l=min(grid[i][j-1],grid[i-1][j])
            grid[i][j]=max(grid[i][j],l)
        elif(0<=i-1<n and 0<=j<n):
            grid[i][j]=max(grid[i][j],grid[i-1][j])
        elif(0<=i<n and 0<=j-1<n):
            grid[i][j]=max(grid[i][j],grid[i][j-1])

print(grid[n-1][n-1])
# Please write your code here.
