import sys
sys.setrecursionlimit(10000)

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
directions = [[1,0],[0,1],[-1,0],[0,-1]]
best_count = 0
pop_count = 0
visited = [[False]*n for _ in range(n)]

def dfs(x,y,k):
    global pop,best_count,count
    if(best_count < count):
            best_count = count
    if(count >= 4):
        pop=True
    for ax,ay in directions:
        nx = ax+x
        ny = ay+y
        if(0<=nx<n and 0<=ny<n):
            if(not visited[ny][nx] and grid[ny][nx]==k):
                visited[ny][nx]=True
                count+=1
                dfs(nx,ny,k)
    
for i in range(n):
    for j in range(n):
        if(not visited[i][j]):
            pop = False
            visited[i][j]=True
            count = 1
            dfs(j,i,grid[i][j])
            if(pop):
                pop_count+=1
                pop=False

print(pop_count,best_count)
# Please write your code here.
