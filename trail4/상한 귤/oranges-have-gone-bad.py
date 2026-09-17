from collections import deque
n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
queue=deque()
visited = [[False]*n for _ in range(n)]
directions = [[0,1],[1,0],[0,-1],[-1,0]] #y,x
t_list=[]
for i in range(n):
    for j in range(n):
        if(grid[i][j]==2):
            t_list.append((i,j))
            visited[i][j]==True
            grid[i][j]=0
        elif(grid[i][j]==0):
            grid[i][j]=-1
for y,x in t_list:
    queue.append((y,x,0))
while queue:
    y,x,second=queue.popleft()

    for ay,ax in directions:
        ny,nx=y+ay,x+ax
        if(0<=nx<n and 0<=ny<n and not visited[ny][nx] and grid[ny][nx]==1):
            visited[ny][nx]=True
            grid[ny][nx]=second+1
            queue.append((ny,nx,second+1))

for i in range(n):
    for j in range(n):
        if(not visited[i][j] and grid[i][j]==1):
            grid[i][j]=-2
for i in range(n):
        print(*grid[i])
