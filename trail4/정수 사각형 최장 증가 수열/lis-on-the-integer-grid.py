n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
direction = [[1,0],[0,1],[0,-1],[-1,0]]#x,y
v_grid = [[-1]*n for _ in range(n)]

def dfs(y,x):
    if(v_grid[y][x] == -1):
        v_grid[y][x]=1
        for ax,ay in direction:
            nx,ny=ax+x,ay+y
            if(0<=nx<n and 0<=ny<n):
                if(grid[ny][nx]>grid[y][x]):
                    v_grid[y][x]=max(v_grid[y][x],dfs(ny,nx)+1)
    return v_grid[y][x]

for i in range(n):
    for j in range(n):
        dfs(i,j)
best=0
for i in range(n):
    for j in range(n):
        if(best<v_grid[i][j]):
            best=v_grid[i][j]
print(best)

# Please write your code here.
