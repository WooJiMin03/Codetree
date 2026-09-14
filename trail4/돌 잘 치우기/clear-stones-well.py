from collections import deque
n, k, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
r = []
c = []
stones=[]
best = 0
for _ in range(k):
    ri, ci = map(int, input().split())
    r.append(ri - 1)
    c.append(ci - 1)
for i in range(n):
    for j in range(n):
        if(grid[i][j]==1):
            stones.append((j,i)) #x,y
m = min(m,len(stones))
queue = deque()
directions=[[1,0],[0,1],[-1,0],[0,-1]]#x,y
c_stones = []

def cleaning(start,count):
    global best,c_stones,queue
    if(count==m):
        m_count=0
        visited = [[False]*n for _ in range(n)]
        for c_x,c_y in c_stones:
            grid[c_y][c_x] = 0
        for d in range(k):
            queue.append((c[d],r[d]))
            visited[r[d]][c[d]]=True 
            m_count+=1
        while(queue):
            x,y=queue.popleft()
            for ax,ay in directions:
                nx,ny=ax+x,ay+y
                if(0<=nx<n and 0<=ny<n and grid[ny][nx]!=1 and not visited[ny][nx]):
                    queue.append((nx,ny))
                    visited[ny][nx]=True 
                    m_count+=1
        if(best < m_count):
            best=m_count
        for c_x,c_y in c_stones:
            grid[c_y][c_x] = 1
        return
    for i in range(start,len(stones)):
        c_stones.append(stones[i])
        cleaning(i+1,count+1)
        c_stones.pop()


cleaning(0,0)
print(best)


# Please write your code here.
