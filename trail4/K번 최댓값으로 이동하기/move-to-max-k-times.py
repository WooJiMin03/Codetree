from collections import deque
n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())
queue = deque()
best=[c-1,r-1,grid[r-1][c-1]]
direction = [[1,0],[0,1],[-1,0],[0,-1]]#x,y
# Please write your code here.
for i in range(k):#여러번 돌려나?
    start_x,start_y,num=best
    next_x=n
    next_y=n
    next_num=0
    visited = [[False]*n for _ in range(n)]
    queue.append((start_x,start_y))
    visited[start_y][start_x]=True
    while queue:
        a,b = queue.popleft()
        for ax,ab in direction:
            n_x,n_y = ax+a,ab+b
            if(0<=n_x<n and 0<=n_y<n and not visited[n_y][n_x]):
                if(grid[n_y][n_x] < num):
                    visited[n_y][n_x]=True
                    queue.append((n_x,n_y))
                    if(grid[n_y][n_x]>next_num):
                        next_num=grid[n_y][n_x]
                        next_x,next_y=n_x,n_y
                    elif(grid[n_y][n_x]==next_num):
                        if(n_y<next_y):
                            next_x,next_y=n_x,n_y
                        elif(n_y==next_y):
                            if(n_x<next_x):
                                next_x,next_y=n_x,n_y
    if(next_num==0):
        break
    best=[next_x,next_y,next_num]
print(best[1]+1,best[0]+1)



