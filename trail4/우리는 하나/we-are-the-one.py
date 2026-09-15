from collections import deque
n, k, u, d = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
best=0
c_list = []
directions=[[1,0],[0,1],[-1,0],[0,-1]]#x,y
queue = deque()

def choose_city(start,count):
    if(count == k):
        global best
        c_count = 0
        visited = [[False]*n for _ in range(n)]
        for j in range(k):
            queue.append((c_list[j]%n,c_list[j]//n))
            visited[c_list[j]//n][c_list[j]%n]=True
            c_count+=1
        while queue:
            x,y=queue.popleft()
            for ax,ay in directions:
                nx,ny=ax+x,ay+y
                if(0<=nx<n and 0<=ny<n and not visited[ny][nx] and u<=abs(grid[y][x]-grid[ny][nx])<=d):
                    queue.append((nx,ny))
                    visited[ny][nx]=True
                    c_count+=1
        if(c_count > best):
            best=c_count
        return

    for i in range(start,n*n):
        c_list.append(i)
        choose_city(i+1,count+1)
        c_list.pop()
choose_city(0,0)
print(best)
# Please write your code here.
