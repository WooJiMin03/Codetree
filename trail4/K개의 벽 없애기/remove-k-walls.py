from collections import deque
n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
r1, c1 = map(int, input().split())
r2, c2 = map(int, input().split())

r1 -= 1
c1 -= 1
r2 -= 1
c2 -= 1

queue=deque()
directions = [[1,0],[0,1],[-1,0],[0,-1]]#x,y
least=float('inf')
rock_list=[]

for i in range(n):
    for j in range(n):
        if(grid[i][j]==1):
            rock_list.append((i,j))
choose_list=[]

def choose_rock(start,count):
    global choose_list
    global least
    if(count==k):
        visited=[[False]*n for _ in range(n)]
        queue.append((c1,r1,0))
        visited[r1][c1]=True
        for r in range(k):
            y,x=choose_list[r]
            grid[y][x]=0

        while queue:
            x,y,step=queue.popleft()
            if(x==c2 and y==r2):
                if(least > step):
                    least=step
                    return
            for ax,ay in directions:
                nx,ny=ax+x,ay+y
                if(0<=nx<n and 0<=ny<n and not visited[ny][nx] and grid[ny][nx] == 0):
                    queue.append((nx,ny,step+1))
                    visited[ny][nx]=True
        for r in range(k):
            y,x=choose_list[r]
            grid[y][x]=1
        return
    for i in range(start,len(rock_list)):
        choose_list.append(rock_list[i])
        choose_rock(i+1,count+1)
        choose_list.pop()
choose_rock(0,0)
if(least==float('inf')):
    least = -1
print(least)
# Please write your code here.
