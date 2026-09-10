import sys
sys.setrecursionlimit(10000)

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
best = 1
max_height = 0
ground_count = 0
directions = [[1,0],[0,1],[-1,0],[0,-1]] #x,y
def dfs(x,y,k,visited):
    for ax,ay in directions:
        nx = x+ax
        ny = y+ay
        if(0<=nx<M and 0<=ny<N):
            if(not visited[ny][nx] and grid[ny][nx]>k):
                visited[ny][nx]=True
                dfs(nx,ny,k,visited)

for i in range(N):
    for j in range(M):
        if(max_height < grid[i][j]):
            max_height = grid[i][j]

for K in range(1,max_height+1):
    visited = [[False]*M for _ in range(N)]
    count = 0
    for i in range(N):
        for j in range(M):
            if(grid[i][j] > K and not visited[i][j]):
                visited[i][j]=True
                dfs(j,i,K,visited)
                count+=1
    if(ground_count < count):
        ground_count=count
        best = K


print(best,ground_count)

# Please write your code here.
