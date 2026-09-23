n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(n-1,-1,-1):
        if(0<=i-1<n and 0<=j+1<n):
            grid[i][j]=grid[i][j]+min(grid[i-1][j],grid[i][j+1])
        elif(0<=j+1<n):
            grid[i][j]=grid[i][j]+grid[i][j+1]
        elif(0<=i-1<n):
            grid[i][j]=grid[i][j]+grid[i-1][j]
print(grid[n-1][0])
# Please write your code here.
